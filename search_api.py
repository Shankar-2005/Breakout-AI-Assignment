import requests
import streamlit as st

def search_entity(entity, prompt_template, api_key):
    search_query = prompt_template.format(entity=entity)
    params = {
        "api_key": api_key,
        "engine": "google",
        "q": search_query
    }
    response = requests.get("https://serpapi.com/search", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Search API request failed. Please check your API key or rate limits.")
        return None
