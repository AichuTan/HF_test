import streamlit as st
st.set_page_config(page_title="Hello Space")
st.title("Hello, Hugging Face Spaces 👋")
name = st.text_input("Your name:")
st.write(f"Welcome, {name or 'friend'}!")

##
##

