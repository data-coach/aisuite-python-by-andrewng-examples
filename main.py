# pip install aisuite[all]

import os
import aisuite as ai
from config import *

# Set API keys as environment variables
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
os.environ['ANTHROPIC_API_KEY'] = ANTHROPIC_API_KEY
os.environ['HUGGINGFACE_TOKEN'] = HF_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY 


client = ai.Client()

# 4.1

messages = [  
    {"role": "system", "content": "You are a creative thinker."},  
    {"role": "user", "content": "Suggest five app ideas that promote sustainable living."}  
]  

response = client.chat.completions.create(model="openai:gpt-4o", messages=messages)  
print("\n".join([f"{i+1}. {idea}" for i, idea in enumerate(response.choices[0].message.content.splitlines())]))

# 4.2

# Specify the Hugging Face model
hf_model = "huggingface:mistralai/Mistral-7B-Instruct-v0.3"

# Prepare the conversation
messages = [
    {"role": "user", "content": "Can you explain the concept of generative AI in simple terms?"}
]

# Generate a response
response = client.chat.completions.create(
    model=hf_model,
    messages=messages
)

# Print the response
print("AI Response:")
print(response.choices[0].message.content)

# 4.3

messages = [  
    {"role": "system", "content": "You are a math tutor."},  
    {"role": "user", "content": "Explain how to solve for x in the equation 2x + 5 = 15."}  
]
groq_llama3_8b = "groq:llama3-8b-8192"
# groq_llama3_70b = "groq:llama3-70b-8192"
response = client.chat.completions.create(model=groq_llama3_8b, messages=messages)
print(response.choices[0].message.content)

# 4.4

messages = [  
    {"role": "system", "content": "You are a sentiment analysis expert."},  
    {"role": "user", "content": "Analyze the sentiment of this review: 'The product quality is excellent, but delivery was delayed.'"}  
]  

response = client.chat.completions.create(model="openai:gpt-4o", messages=messages)  
print(response.choices[0].message.content)