import os
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Create list to hold user input
system_prompt_inputs = []

# Create input fields
for i in range(1, 11):
    system_prompt_inputs.append(st.text_input(f"Please enter prompt part {i}:"))

# Combine inputs into a single system prompt
system_prompt = ' '.join(system_prompt_inputs)

# The 'system' message to set up the assistant's behavior
system_message = {"role": "system", "content": system_prompt}

def ask_gpt3(question):
    user_message = {"role": "user", "content": question}
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",  
        messages=[system_message, user_message]
    )
    
    return response.choices[0].message['content']

st.title('Talk to Yourself')

question = st.text_input("Please enter your question:")
if st.button('Ask'):
    st.write("Thinking...")
    response = ask_gpt3(question)
    st.write(response)
