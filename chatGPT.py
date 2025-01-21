# import openai

# Ensure you have your API key set


from openai import OpenAI
import os

# client = OpenAI()
_my_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = _my_api_key)
class CChatGPT:
    def __init__(self):
        pass

    def sendMessage(self,msg):
        pass
        return 0



completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)