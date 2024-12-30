import os
from github import Github
import time

def watch_repositories():
    # Initialize GitHub client
    gh = Github(os.getenv('GITHUB_TOKEN'))
    user = gh.get_user('ZubeidHendricks')
    
    # Get all repositories
    repositories = user.get_repos()
    
    for repo in repositories:
        # Check for issues with ai-development label
        issues = repo.get_issues(labels=['ai-development'])
        
        for issue in issues:
            if not has_been_processed(issue):
                process_issue(repo, issue)

def has_been_processed(issue):
    # Check if issue already has a PR or is in progress
    return any(label.name in ['in-progress', 'completed'] for label in issue.labels)

def process_issue(repo, issue):
    # Mark issue as in progress
    issue.add_to_labels('in-progress')
    
    # Trigger AI development workflow
    repo.create_repository_dispatch(
        'ai-development-task',
        {
            'repository': f'{repo.owner.login}/{repo.name}',
            'issue_number': issue.number
        }
    )

if __name__ == '__main__':
    while True:
        try:
            watch_repositories()
        except Exception as e:
            print(f'Error: {e}')
        time.sleep(300)  # Check every 5 minutes