# AI Dev Orchestrator

AI-powered development workflow automation tool that generates code, tests, and documentation.

## Components

1. Development Agents:
- Frontend Developer
- Backend Developer
- Database Engineer
- Testing Specialist

2. Tools:
- Code Generation
- Test Generation
- Documentation Generation
- Schema Generation

3. Workflows:
- Task Analysis
- Code Generation
- Test Creation
- PR Creation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export LLAMA_MODEL_PATH=path/to/model
export GITHUB_TOKEN=your_token
```

3. Run the orchestrator:
```bash
python src/main.py
```

## Usage

1. Create an issue with the 'ai-development' label
2. Add specifications in the issue description
3. The system will:
   - Analyze the requirements
   - Generate code and tests
   - Create a pull request
   - Update the issue with results

## Contributing

1. Fork the repository
2. Create your feature branch
3. Submit a pull request
