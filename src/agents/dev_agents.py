from src.tools.frontend_tools import FrontendTools
from src.tools.backend_tools import BackendTools
from src.tools.database_tools import DatabaseTools
from src.tools.testing_tools import TestingTools

class DevelopmentAgents:
    def __init__(self, llm):
        self.llm = llm
        self.tools = self.setup_tools()
    
    def setup_tools(self):
        return {
            'frontend': FrontendTools(self.llm),
            'backend': BackendTools(self.llm),
            'database': DatabaseTools(self.llm),
            'testing': TestingTools(self.llm)
        }
    
    def get_agent(self, task_type):
        if task_type == 'frontend':
            return self.create_frontend_agent()
        elif task_type == 'backend':
            return self.create_backend_agent()
        elif task_type == 'database':
            return self.create_database_agent()
        elif task_type == 'testing':
            return self.create_testing_agent()
        raise ValueError(f"Unknown task type: {task_type}")
    
    def create_frontend_agent(self):
        return Agent(
            role='Frontend Developer',
            goal='Implement high-quality frontend features',
            backstory='Senior frontend developer with expertise in React and modern frontend practices',
            tools=[self.tools['frontend']],
            llm=self.llm
        )

    def create_backend_agent(self):
        return Agent(
            role='Backend Developer',
            goal='Implement robust backend services',
            backstory='Senior backend developer with expertise in API design and server architecture',
            tools=[self.tools['backend']],
            llm=self.llm
        )