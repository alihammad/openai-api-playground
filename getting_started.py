import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENAI_API_KEY:
#     raise ValueError("OPENAI_API_KEY not set in .env file.")

# openai.api_key = OPENAI_API_KEY
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