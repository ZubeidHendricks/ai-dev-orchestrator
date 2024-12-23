from src.agents.dev_agents import DevelopmentAgents

class TaskHandler:
    def __init__(self, llm):
        self.agents = DevelopmentAgents(llm)
    
    def handle_task(self, task):
        # Determine task type
        task_type = self.get_task_type(task)
        
        # Get appropriate agent
        agent = self.agents.get_agent(task_type)
        
        # Generate code
        code = agent.execute(task)
        
        # Generate tests
        tests = self.agents.tools['testing'].generate_tests(code)
        
        return {
            'code': code,
            'tests': tests,
            'task_type': task_type
        }
    
    def get_task_type(self, task):
        # Analyze task description to determine type
        if any(kw in task.lower() for kw in ['ui', 'component', 'frontend']):
            return 'frontend'
        elif any(kw in task.lower() for kw in ['api', 'endpoint', 'backend']):
            return 'backend'
        elif any(kw in task.lower() for kw in ['database', 'model', 'schema']):
            return 'database'
        return 'general'