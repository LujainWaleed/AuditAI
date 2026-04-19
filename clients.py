import os
import streamlit as st
from openai import OpenAI


@st.cache_resource
def get_groq_client() -> OpenAI:
    """Return a cached OpenAI-compatible client pointed at Groq."""
    return OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY", "xxxx"),
    )