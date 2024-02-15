from langchain.llms import openai
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
# function to load huggingface model

def get_responses(questions):
    llm=openai(openai_api_key=os.environ['OPEN_API_KEY'],model_name="text-davinci-003")