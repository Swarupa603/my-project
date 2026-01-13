import streamlit as st
st.title("some basic commands like slider button etc")
age = st.slider("select your age",1,100)
city=st.selectbox("choose your city",["mumbai","delhi","pune","bangalore"])
if st.button("show details"):
    st.write("age:",age)
    st.write("city:",city)