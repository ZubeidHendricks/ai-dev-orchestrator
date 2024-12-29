from groq import Groq
import os

class LLMService:
    def __init__(self):
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY")
        )
    
    def generate_code(self, prompt):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama3-70b-8192"  # Groq's Llama 70B model
            )
            
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Error generating code: {e}")
            return None

    # Add other LLM methods as needed
