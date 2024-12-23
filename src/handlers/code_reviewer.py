import os
from github import Github

def review_code():
    # Get GitHub token
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        raise ValueError("Missing GitHub token")
    
    # Initialize GitHub client
    gh = Github(github_token)
    repo = gh.get_repo(os.getenv('GITHUB_REPOSITORY', 'ZubeidHendricks/ai-dev-orchestrator'))
    
    # Get pull request
    pr_number = get_pr_number()
    if not pr_number:
        print("No pull request found")
        return
    
    pr = repo.get_pull(pr_number)
    
    # Review changes
    review_comments = []
    for file in pr.get_files():
        comments = review_file(file)
        if comments:
            review_comments.extend(comments)
    
    # Add review comments
    if review_comments:
        pr.create_review(
            body="\n".join(review_comments),
            event='COMMENT'
        )

def get_pr_number():
    # Get PR number from environment or latest PR
    return int(os.getenv('PR_NUMBER', 0))

def review_file(file):
    comments = []
    
    # Basic file checks
    if file.filename.endswith('.py'):
        comments.extend(review_python_file(file))
    elif file.filename.endswith('.js'):
        comments.extend(review_javascript_file(file))
    
    return comments

def review_python_file(file):
    comments = []
    
    # Add Python-specific checks
    content = file.decoded_content.decode()
    
    # Check for basic issues
    if 'print(' in content:
        comments.append(f"Consider using logging instead of print statements in {file.filename}")
    
    if 'except:' in content:
        comments.append(f"Avoid bare except clauses in {file.filename}")
    
    return comments

def review_javascript_file(file):
    comments = []
    
    # Add JavaScript-specific checks
    content = file.decoded_content.decode()
    
    # Check for basic issues
    if 'var ' in content:
        comments.append(f"Consider using 'let' or 'const' instead of 'var' in {file.filename}")
    
    if 'console.log(' in content:
        comments.append(f"Remember to remove console.log statements in {file.filename}")
    
    return comments

if __name__ == '__main__':
    review_code()