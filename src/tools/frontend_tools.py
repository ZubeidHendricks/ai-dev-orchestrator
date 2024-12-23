class FrontendTools:
    def __init__(self, llm):
        self.llm = llm
    
    def generate_component(self, specs):
        prompt = f"""
        Create a React component based on these specifications:
        {specs}
        Include:
        - TypeScript types
        - Props interface
        - Error handling
        - Loading states
        - Basic styling
        - Unit tests
        """
        return self.llm(prompt)
    
    def generate_styles(self, specs):
        prompt = f"""
        Generate styles for component:
        {specs}
        Include:
        - Responsive design
        - Dark/light mode support
        - Accessibility features
        """
        return self.llm(prompt)