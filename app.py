# importing libraries
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

#configure API_KEY
genai.configure(api_key=os.getenv('API_KEY'))
#loading the model
model = genai.GenerativeModel('gemini-pro')

#streamlit page
st.set_page_config(page_title='Gemini Pro Chatbot')
st.header('ChatBot') # page header
st.write('You are now chatting with Gemini-Pro, Google\'s GenAI.')

#startchat  session
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    st.session_state['chat'] = model.start_chat(history=[])

user_input = st.text_input('Enter text') # text field
submit = st.button('Send') # button
clear_chat = st.button('Clear chat')# button

# code to handle clear chat feature
if clear_chat:
    st.session_state['chat_history'] = []
    st.session_state['chat'] = model.start_chat(history=[])

#code to handle chat with chat bot feature
if submit and user_input:
    st.session_state['chat_history'].append(('User', user_input)) # appending user input message to the session chat history
    response = st.session_state['chat'].send_message(user_input)
    st.session_state['chat_history'].append(('Gemini', response.text)) # appending gemini response to the session chat history

    for user, chat in st.session_state['chat_history']:
        st.write(f'{user}: {chat}') # writing the chat history on web page