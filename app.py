import streamlit as st

st.title("Milky Way Matchmaking")
uploaded_file = st.file_uploader("Upload your resume here")

if uploaded_file:
    st.text("We have your Resume")
