import openai

# Replace with your actual API key
api_key = "your_api_key_here"

response = openai.ChatCompletion.create(
    model="gpt-4",  # Use "gpt-3.5-turbo" for a cheaper option
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about AI."}
    ],
    max_tokens=100
)

print(response['choices'][0]['message']['content'])
