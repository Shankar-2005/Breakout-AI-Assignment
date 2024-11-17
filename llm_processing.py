import openai
import streamlit as st
import time

def extract_info_with_llm(search_results, extraction_prompt, api_key):
    openai.api_key = api_key
    
    # Build conversation-style message
    messages = [
        {"role": "system", "content": "You are an AI assistant trained to extract specific information from provided text."},
        {"role": "user", "content": extraction_prompt + "\n\n" + " ".join([result['snippet'] for result in search_results['organic_results'][:5]])}
    ]
    
    # Retry loop for rate limits
    for attempt in range(3):  # Retry up to 3 times
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=100,
                temperature=0.5
            )
            return response.choices[0].message["content"].strip()
        
        except openai.error.RateLimitError:
            st.warning("Rate limit exceeded. Retrying in 30 seconds...")
            time.sleep(30)  # Wait 30 seconds and retry
    
    st.error("Failed to retrieve data due to rate limits. Please try again later.")
    return None
