import os
import sys
import json

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.llm_service import LLMService

def main():
    # Initialize LLM Service
    llm_service = LLMService()
    
    # Example task analysis
    task_description = "Create a flexible web scraping utility"
    
    # Generate code
    generated_code = llm_service.generate_code(task_description)
    
    # Print or further process the generated code
    print("Generated Code:")
    print(generated_code)

if __name__ == "__main__":
    main()
