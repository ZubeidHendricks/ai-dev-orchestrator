import os
from github import Github
import groq

def analyze_issue():
    # Get environment variables
    github_token = os.getenv('GITHUB_TOKEN')
    groq_api_key = os.getenv('GROQ_API_KEY')
    target_repo = os.getenv('TARGET_REPO')
    issue_number = os.getenv('ISSUE_NUMBER')
    
    if not all([github_token, groq_api_key, target_repo, issue_number]):
        raise ValueError("Missing required environment variables")
    
    # Initialize clients
    gh = Github(github_token)
    groq_client = groq.Groq(api_key=groq_api_key)
    
    # Get issue details
    repo = gh.get_repo(target_repo)
    issue = repo.get_issue(number=int(issue_number))
    
    # Determine project type
    project_type = determine_project_type(repo)
    
    # Analyze issue with Groq
    analysis = analyze_with_groq(groq_client, issue, project_type)
    
    # Save analysis results
    save_analysis(analysis)

def determine_project_type(repo):
    # Check repository for project type indicators
    files = repo.get_contents('')
    file_names = [f.name for f in files]
    
    if any(f.endswith('.csproj') for f in file_names):
        return 'dotnet'
    elif 'package.json' in file_names:
        return 'node'
    elif 'requirements.txt' in file_names:
        return 'python'
    else:
        return 'unknown'

def get_project_prompt(project_type):
    prompts = {
        'dotnet': """You are a senior .NET architect specializing in:
            - C# development
            - Blazor WebAssembly
            - .NET Core APIs
            - Entity Framework Core
            Generate implementation plans following .NET best practices.""",
        'node': """You are a senior JavaScript/TypeScript developer specializing in:
            - Node.js backend development
            - React/Next.js frontend
            - RESTful APIs
            Generate implementation plans following JavaScript best practices.""",
        'python': """You are a senior Python developer specializing in:
            - FastAPI/Flask development
            - SQLAlchemy
            - Python best practices
            Generate implementation plans following Python best practices.""",
        'unknown': "You are a senior software architect. Analyze the requirements and suggest appropriate technology stack."
    }
    return prompts.get(project_type, prompts['unknown'])

def analyze_with_groq(client, issue, project_type):
    # Get appropriate system prompt
    system_prompt = get_project_prompt(project_type)
    
    # Prepare the task prompt
    task_prompt = f"""
    Analyze this development task and provide detailed implementation plan:

    Repository Type: {project_type}
    Title: {issue.title}
    Description: {issue.body}
    Labels: {[label.name for label in issue.labels]}

    Provide detailed analysis including:
    1. Technical implementation details
    2. Required classes and methods
    3. Test requirements
    4. Integration points
    5. Performance criteria
    """
    
    # Get analysis from Groq
    response = client.chat.completions.create(
        messages=[{
            "role": "system",
            "content": system_prompt
        }, {
            "role": "user",
            "content": task_prompt
        }],
        model="mixtral-8x7b-32768",
        temperature=0.3,
        max_tokens=2000
    )
    
    # Extract and structure the analysis
    analysis = {
        'title': issue.title,
        'description': issue.body,
        'project_type': project_type,
        'labels': [label.name for label in issue.labels],
        'requirements': response.choices[0].message.content,
        'type': determine_task_type(issue)
    }
    
    return analysis

def determine_task_type(issue):
    labels = [label.name.lower() for label in issue.labels]
    
    if 'frontend' in labels:
        return 'frontend'
    elif 'backend' in labels:
        return 'backend'
    elif 'bug' in labels:
        return 'bug'
    return 'feature'

def save_analysis(analysis):
    # Create analysis directory if it doesn't exist
    os.makedirs('analysis', exist_ok=True)
    
    # Save analysis results
    with open(f"analysis/latest.txt", 'w') as f:
        f.write(str(analysis))
    
    filename = f"analysis/task_{analysis['title'].lower().replace(' ', '_')}.txt"
    with open(filename, 'w') as f:
        for key, value in analysis.items():
            f.write(f"{key}:\n{value}\n\n")

if __name__ == '__main__':
    analyze_issue()