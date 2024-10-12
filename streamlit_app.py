import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = "http://0.0.0.0:8000/v1/pw_ai_answer"

def get_response(prompt):
    headers = {
        "accept": "*/*",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    return response.json()

st.markdown("<h1 style='text-align: center;'>D-ai-Lysis</h1>", unsafe_allow_html=True)
st.write("An AI-driven medical assistant offering intelligent support for patient care and health management.")

prompt = st.text_input("Enter your prompt:")
if st.button("Get Response"):
    if prompt:
        response = get_response(prompt)
        
        # Display the response in a nice-looking box with markdown and a subtle background
        st.markdown("""
        <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; margin-top: 10px;">
            <h4 style="color: #00FFFF;">Response:</h4>
            <p style="color: white; font-size: 16px;">{}</p>
        </div>
        """.format(response), unsafe_allow_html=True)
    else:
        st.write("Please enter a prompt.")



