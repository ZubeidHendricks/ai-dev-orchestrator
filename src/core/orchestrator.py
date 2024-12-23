from src.generators.code_generator import CodeGenerator
from src.security.vulnerability_scanner import SecurityScanner
from src.testing.test_generator import TestGenerator
from src.workflow.pipeline import DevOrchestrator

class AIDevOrchestrator:
    def __init__(self):
        self.code_generator = CodeGenerator()
        self.security_scanner = SecurityScanner()
        self.test_generator = TestGenerator()
        self.workflow = DevOrchestrator()
    
    def execute_project(self, project_requirements):
        generated_code = self.code_generator.generate_code(project_requirements)
        security_results = self.security_scanner.scan_code(generated_code)
        test_cases = self.test_generator.generate_tests(generated_code)
        
        self.workflow.run_development_pipeline({
            'code': generated_code,
            'security_results': security_results,
            'test_cases': test_cases
        })
