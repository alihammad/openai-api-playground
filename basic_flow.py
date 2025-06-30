import os
import openai
from IPython.display import display, Markdown
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = openai.OpenAI()  # Uses your OPENAI_API_KEY from environment

# Converse with GPT with openai.ChatCompletion.create()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
            "role": "system",
            "content": 'You are a stand-up comic performing to an audience of data    scientists. Your specialist genre is dad jokes.'
        }, {
            "role": "user",
            "content": 'Tell a joke about statistics.'
        }, {
            "role": "assistant",
            "content": 'My last was gig at a statistics conference. I told 100 jokes to try       and make people laugh. No pun in ten did.'
        }
     ]
)

# Check the response status
print("Finish Reason: " + response.choices[0].finish_reason)

# Render the AI output content
print(response.choices[0].message.content)

# Control randomness with temperature (default is 1)
# temperature=0 gives highly deterministic output
# temperature=2 gives highly random output
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
            "role": "system",
            "content": 'You are a stand-up comic performing to an audience of data    scientists. Your specialist genre is dad jokes.'
        }, {
            "role": "user",
            "content": 'Tell a joke about statistics.'
        }, {
            "role": "assistant",
            "content": 'My last was gig at a statistics conference. I told 100 jokes to try       and make people laugh. No pun in ten did.'
        }
     ], 
     temperature=0.5
)

print("Response with temperature control:0.5")
print(response.choices[0].message.content)
print("---------------------")

# Control randomness using nucleus sampling with top_p (default is 1)
# top_p = 0 gives highly deterministic output
# top_p = 1 gives highly random output
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
            "role": "system",
            "content": 'You are a stand-up comic performing to an audience of data    scientists. Your specialist genre is dad jokes.'
        }, {
            "role": "user",
            "content": 'Tell a joke about statistics.'
        }, {
            "role": "assistant",
            "content": 'My last was gig at a statistics conference. I told 100 jokes to try       and make people laugh. No pun in ten did.'
        }
     ], 
    top_p=0.5
)


print("Response with top_p control:0.5")
print(response.choices[0].message.content)
print("---------------------")

# Control talking about new topics using presence_penalty (default is 0)
# presence_penalty=-2 gives more repetition in conversations
# presence_penalty=2 gives more novelty in conversations
# frequency_penalty behaves similarly, but counts number of instances 
# of previous tokens rather than detecting their presence
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
            "role": "system",
            "content": 'You are a stand-up comic performing to an audience of data    scientists. Your specialist genre is dad jokes.'
        }, {
            "role": "user",
            "content": 'Tell a joke about statistics.'
        }, {
            "role": "assistant",
            "content": 'My last was gig at a statistics conference. I told 100 jokes to try       and make people laugh. No pun in ten did.'
        }
     ], 
     presence_penalty=1
)

print("Response with presence_penalty control:1")
print(response.choices[0].message.content)
print("---------------------")

# Limit output length with max_tokens
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
            "role": "system",
            "content": 'You are a stand-up comic performing to an audience of data    scientists. Your specialist genre is dad jokes.'
        }, {
            "role": "user",
            "content": 'Tell a joke about statistics.'
        }, {
            "role": "assistant",
            "content": 'My last was gig at a statistics conference. I told 100 jokes to try       and make people laugh. No pun in ten did.'
        }
     ], 
      max_tokens=500
)


print("Response with max_tokens:500")
print(response.choices[0].message.content)
print("---------------------")