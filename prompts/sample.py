from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(
    model = 'gemini-3.1-flash-lite',
    api_key = os.getenv("gemini_api")
    )
#result = model.invoke("Write a poem on cricket")
st.header(" Research Summarizer ")
user_inp = st.text_input('Enter your prompt : ')

if st.button('Summarise'):
    result = model.invoke(user_inp)
    st.text(result.content[0]["text"])
