import streamlit as st
import google.generativeai as genai

st.title("Welcome to generative ai")

user_input=st.text_input("ask me anything")
genai.configure(api_key="AIzaSyDrrNrYDUCOVwvGoW2Evgy0IGZVLf5DkBs")