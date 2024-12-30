import os
from github import Github
import groq

def analyze_issue():
    # Get environment variables
    github_token = os.getenv('GITHUB_TOKEN')
    groq_api_key = os.getenv('GROQ_API_KEY')
    issue_number = os.getenv('ISSUE_NUMBER')
    
    if not all([github_token, groq_api_key, issue_number]):
        raise ValueError("Missing required environment variables")
    
    # Initialize clients
    gh = Github(github_token)
    groq_client = groq.Groq(api_key=groq_api_key)
    
    # Get issue details
    repo = gh.get_repo(os.getenv('GITHUB_REPOSITORY', 'ZubeidHendricks/ai-dev-orchestrator'))
    issue = repo.get_issue(number=int(issue_number))
    
    # Analyze issue with Groq
    analysis = analyze_with_groq(groq_client, issue)
    
    # Save analysis results
    save_analysis(analysis)

def analyze_with_groq(client, issue):
    # Prepare the prompt
    prompt = f"""
    Analyze the following development task and provide structured requirements:

    Title: {issue.title}
    Description: {issue.body}
    Labels: {[label.name for label in issue.labels]}

    Please provide:
    1. Technical requirements
    2. Implementation approach
    3. Testing requirements
    4. Integration points
    5. Success criteria
    """
    
    # Get analysis from Groq
    response = client.chat.completions.create(
        messages=[{
            "role": "system",
            "content": "You are a technical analyst specialized in software development requirements analysis."
        }, {
            "role": "user",
            "content": prompt
        }],
        model="mixtral-8x7b-32768",
        temperature=0.3,
        max_tokens=2000
    )
    
    # Extract and structure the analysis
    analysis = {
        'title': issue.title,
        'description': issue.body,
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
    filename = f"analysis/task_{analysis['title'].lower().replace(' ', '_')}.txt"
    with open(filename, 'w') as f:
        for key, value in analysis.items():
            f.write(f"{key}:\n{value}\n\n")

if __name__ == '__main__':
    analyze_issue()