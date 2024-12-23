import os
from github import Github

def analyze_issue():
    # Get GitHub token and issue number
    github_token = os.getenv('GITHUB_TOKEN')
    issue_number = os.getenv('ISSUE_NUMBER')
    
    if not github_token or not issue_number:
        raise ValueError("Missing required environment variables")
    
    # Initialize GitHub client
    gh = Github(github_token)
    repo = gh.get_repo(os.getenv('GITHUB_REPOSITORY', 'ZubeidHendricks/ai-dev-orchestrator'))
    issue = repo.get_issue(number=int(issue_number))
    
    # Analyze issue content
    analysis = {
        'title': issue.title,
        'description': issue.body,
        'labels': [label.name for label in issue.labels],
        'type': determine_task_type(issue),
        'requirements': extract_requirements(issue.body)
    }
    
    # Save analysis results
    save_analysis(analysis)
    
def determine_task_type(issue):
    labels = [label.name.lower() for label in issue.labels]
    
    if 'frontend' in labels:
        return 'frontend'
    elif 'backend' in labels:
        return 'backend'
    elif 'bug' in labels:
        return 'bug'
    return 'feature'

def extract_requirements(body):
    # Extract requirements from issue description
    lines = body.split('\n')
    requirements = []
    
    for line in lines:
        if line.strip().startswith('- [ ]') or line.strip().startswith('* '):
            requirements.append(line.strip().replace('- [ ] ', '').replace('* ', ''))
    
    return requirements

def save_analysis(analysis):
    # Create analysis directory if it doesn't exist
    os.makedirs('analysis', exist_ok=True)
    
    # Save analysis results
    with open(f"analysis/task_{analysis['title'].lower().replace(' ', '_')}.txt", 'w') as f:
        for key, value in analysis.items():
            f.write(f"{key}: {value}\n")

if __name__ == '__main__':
    analyze_issue()