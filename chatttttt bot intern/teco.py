from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from streamlit_pills import pills

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Please set GEMINI_API_KEY in your .env file")
    st.stop()

# Initialize Gemini-Pro 
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

st.title("Testing chat")
selected = pills("how can i help you?",["can you tell joke?", "what is python", "what are vowels?"],["🍪", "⛅", "📝"])
#st.write(selected)


#giving role to streamlit of assistant & gemini uses model for assistant
def role_to_streamlit(role):
  if role == "model":
     return "assistant"
  else:
     return role

#ADD OBJECT WHERE chat history will be saved
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])
    
#both bot and user history sAVE TGT (will not save alone)

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
        



#markdown prompt and icon of user
if prompt := st.chat_input("write heereee"):
    st.chat_message("user").markdown(prompt)  #user = icon and messages belongs to user
    
    


#response of user chat (gemini will read users message)
    response = st.session_state.chat.send_message(prompt) 
    
    with st.chat_message("assistant"):
        st.markdown(response.text)

    
elif selected:
    response = st.session_state.chat.send_message(selected)
    


#for assistant icon and response
    with st.chat_message("assistant"):
        st.markdown(response.text)
