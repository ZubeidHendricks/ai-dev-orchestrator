class TestingTools:
    def __init__(self, llm):
        self.llm = llm
    
    def generate_tests(self, code):
        prompt = f"""
        Create tests for:
        {code}
        Include:
        - Unit tests
        - Integration tests
        - Edge cases
        - Error scenarios
        - Mock examples
        """
        return self.llm(prompt)
    
    def generate_e2e_tests(self, specs):
        prompt = f"""
        Create end-to-end tests for:
        {specs}
        Include:
        - User flows
        - Setup/teardown
        - Test data
        - Assertions
        """
        return self.llm(prompt)