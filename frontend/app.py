import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Lambda Function Executor")

menu = ["Create Function", "Execute Function"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Function":
    name = st.text_input("Function Name")
    code = st.text_area("Function Code", "print('Hello from Lambda')")
    language = st.selectbox("Language", ["python"])
    timeout = st.slider("Timeout (sec)", 1, 10, 5)
    if st.button("Save Function"):
        res = requests.post(f"{API_URL}/functions", json={
            "name": name,
            "code": code,
            "language": language,
            "timeout": timeout
        })
        st.success(res.json())

elif choice == "Execute Function":
    name = st.text_input("Function Name to Execute")
    if st.button("Run"):
        res = requests.post(f"{API_URL}/functions/{name}/execute")
        st.code(res.json().get("output", "No output"))