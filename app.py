import streamlit as st

st.title("🎈 My First Streamlit App")
st.write("Hello, Streamlit!")

name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.write(f"Hello, {name}!")