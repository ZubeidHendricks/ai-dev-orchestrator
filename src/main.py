import os
from pathlib import Path
from github import Github
from langchain.llms import LlamaCpp

def setup_llm():
    model_path = os.getenv('LLAMA_MODEL_PATH', 'models/llama-2-70b-chat.gguf')
    
    # Check if model exists
    if not Path(model_path).exists():
        raise FileNotFoundError(f"LLM model not found at {model_path}")
    
    return LlamaCpp(
        model_path=model_path,
        n_gpu_layers=40,
        n_batch=512,
        n_ctx=4096,
        temperature=0.7
    )

def generate_code():
    # Get analysis results
    analysis = get_analysis()
    if not analysis:
        raise ValueError("No analysis results found")
    
    # Setup LLM
    try:
        llm = setup_llm()
    except FileNotFoundError:
        print("LLM model not found, using fallback method")
        return generate_code_fallback(analysis)
    
    # Generate code based on analysis
    code = generate_implementation(llm, analysis)
    tests = generate_tests(llm, code)
    
    # Save generated code
    save_code(code, tests)

def get_analysis():
    # Get latest analysis file
    analysis_dir = Path('analysis')
    if not analysis_dir.exists():
        return None
    
    analysis_files = list(analysis_dir.glob('*.txt'))
    if not analysis_files:
        return None
    
    latest_file = max(analysis_files, key=lambda f: f.stat().st_mtime)
    
    # Read analysis
    analysis = {}
    with open(latest_file) as f:
        for line in f:
            key, value = line.strip().split(': ', 1)
            analysis[key] = value
    
    return analysis

def generate_implementation(llm, analysis):
    prompt = f"""
    Create implementation based on:
    Title: {analysis['title']}
    Type: {analysis['type']}
    Requirements:
    {analysis['requirements']}
    
    Include:
    - Error handling
    - Input validation
    - Documentation
    """
    
    return llm(prompt)

def generate_tests(llm, code):
    prompt = f"""
    Generate tests for:
    {code}
    
    Include:
    - Unit tests
    - Edge cases
    - Error cases
    """
    
    return llm(prompt)

def generate_code_fallback(analysis):
    # Simple template-based fallback
    if analysis['type'] == 'frontend':
        return generate_frontend_template(analysis)
    elif analysis['type'] == 'backend':
        return generate_backend_template(analysis)
    return generate_feature_template(analysis)

def save_code(code, tests):
    # Create directories
    Path('generated/code').mkdir(parents=True, exist_ok=True)
    Path('generated/tests').mkdir(parents=True, exist_ok=True)
    
    # Save files
    with open('generated/code/implementation.py', 'w') as f:
        f.write(code)
    
    with open('generated/tests/test_implementation.py', 'w') as f:
        f.write(tests)

def generate_frontend_template(analysis):
    return """
    import React from 'react';
    
    interface Props {}
    
    export const Component: React.FC<Props> = () => {
        return <div>Implementation needed</div>;
    };
    """

def generate_backend_template(analysis):
    return """
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    async def root():
        return {"message": "Implementation needed"}
    """

def generate_feature_template(analysis):
    return """
    def implement_feature():
        # Implementation needed
        pass
    """

if __name__ == '__main__':
    generate_code()