from groq import Groq
import os

class LLMService:
    def __init__(self):
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        
        self.client = Groq(api_key=api_key)
    
    def generate_code(self, prompt):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant that generates clean, efficient Python code."
                    },
                    {
                        "role": "user",
                        "content": f"Generate a Python implementation for the following task: {prompt}"
                    }
                ],
                model="llama3-70b-8192"  # Groq's Llama 70B model
            )
            
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Error generating code: {e}")
            return f"Error: {str(e)}"