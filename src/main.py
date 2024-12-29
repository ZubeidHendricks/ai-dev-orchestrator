import os
import sys
import json

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.llm_service import LLMService

def main():
    # Check for Groq API key
    groq_api_key = os.environ.get('GROQ_API_KEY')
    if not groq_api_key:
        print("Error: GROQ_API_KEY environment variable is not set.")
        sys.exit(1)
    
    # Initialize LLM Service
    llm_service = LLMService()
    
    # Get issue details from GitHub context
    github_context = os.environ.get('GITHUB_CONTEXT', '{}')
    try:
        context = json.loads(github_context)
        task_description = context.get('event', {}).get('issue', {}).get('body', 'Create a generic utility')
    except Exception as e:
        print(f"Error parsing GitHub context: {e}")
        task_description = "Create a generic utility"
    
    # Generate code
    generated_code = llm_service.generate_code(task_description)
    
    # Print or further process the generated code
    print("Generated Code:")
    print(generated_code)

if __name__ == "__main__":
    main()