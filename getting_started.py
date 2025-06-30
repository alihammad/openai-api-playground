import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

client = openai.OpenAI()  # Uses your OPENAI_API_KEY from environment

# Example: Send a simple prompt to ChatGPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, ChatGPT!"}]
)

print("ChatGPT response:", response.choices[0].message.content)
print()

# List available models
models = client.models.list()
for model in models.data:
    print(model.id)