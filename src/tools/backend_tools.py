class BackendTools:
    def __init__(self, llm):
        self.llm = llm
    
    def generate_api(self, specs):
        prompt = f"""
        Create an API endpoint based on these specifications:
        {specs}
        Include:
        - Input validation
        - Error handling
        - Status codes
        - Response types
        - Security measures
        - Unit tests
        """
        return self.llm(prompt)
    
    def generate_model(self, specs):
        prompt = f"""
        Create a data model based on:
        {specs}
        Include:
        - Field types
        - Validation rules
        - Database indexes
        - Relationships
        - Migration script
        """
        return self.llm(prompt)