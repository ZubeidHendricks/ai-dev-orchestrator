class DatabaseTools:
    def __init__(self, llm):
        self.llm = llm
    
    def generate_schema(self, specs):
        prompt = f"""
        Create a database schema based on:
        {specs}
        Include:
        - Tables
        - Fields and types
        - Relationships
        - Indexes
        - Constraints
        """
        return self.llm(prompt)
    
    def generate_migration(self, changes):
        prompt = f"""
        Create a database migration for:
        {changes}
        Include:
        - Up migration
        - Down migration
        - Data preservation
        """
        return self.llm(prompt)