
#ytreeuwuwuw
import streamlit as st
from streamlit_google_auth import Authenticate

import os
import dotenv
dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llama_api_key = os.getenv("LLAMA_API_KEY")


# Llamaindex and openai import
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-4o", api_key=openai_api_key)

chat_text=""

st.title('Streamlit Google Auth Example')

authenticator = Authenticate(
    secret_credentials_path = 'google_credentials.json',
    cookie_name='my_cookie_name',
    cookie_key='this_is_secret',
   # redirect_uri = 'https://appappprojecti-qrz5znd5jopech6kfqxs5b.streamlit.app',

    #redirect_uri = 'https://appappprojecti-qrz5znd5jopech6kfqxs5b.streamlit.app',
    redirect_uri = 'http://localhost:8501',
)

# Catch the login event
authenticator.check_authentification()

# Create the login button
authenticator.login()

if st.session_state['connected']:
    st.image(st.session_state['user_info'].get('picture'))
    st.write('Hello, '+ st.session_state['user_info'].get('name'))
    st.write('Your email is '+ st.session_state['user_info'].get('email'))

# The following executes after successful login via Google Cloud Authentication using gmail
    chat_text = st.text_area("Chat with your AI assistant", key="chat_text")
    llm_response = llm.complete(chat_text)
    st.write(llm_response)





    if st.button('Log out'):
        authenticator.logout()