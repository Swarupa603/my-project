import streamlit as st

title = "My Streamlit App"
st.title(title)
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")