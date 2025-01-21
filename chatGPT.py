from openai import OpenAI
import os

class CChatGPT:
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model

    def send_message(self, msg):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": msg}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"

# Usage example
if __name__ == "__main__":
    chat_gpt = CChatGPT()
    response = chat_gpt.send_message("Write a haiku about recursion in programming.")
    print(response)
