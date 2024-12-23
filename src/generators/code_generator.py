from crewai import Agent, Task, Crew

class CodeGenerator:
    def __init__(self):
        self.code_writer = Agent(
            role='Code Writer',
            goal='Generate high-quality code',
            backstory='Expert in multiple programming languages'
        )

    def generate_code(self, project_requirements):
        code_generation_task = Task(
            description=f'Generate code for: {project_requirements}',
            agent=self.code_writer
        )

        crew = Crew(
            agents=[self.code_writer],
            tasks=[code_generation_task]
        )

        return crew.kickoff()
