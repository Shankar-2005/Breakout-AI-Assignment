import requests
import streamlit as st
import time

def extract_info_with_llm(search_results, extraction_prompt, api_key):
    # Combine search results snippets into a single prompt format
    user_input = extraction_prompt + "\n\n" + "\n".join([result['snippet'] for result in search_results['organic_results'][:5]])

    # Set up headers with the Groq API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Define payload with the 'model' property
    payload = {
        "model": "llama3-8b-8192",  
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."}, 
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 100,          
        "temperature": 0.5          
    }

    # Groq API endpoint 
    endpoint = "https://api.groq.com/openai/v1/chat/completions" 

    max_retries = 3
    timeout = 15 
    retry_count = 0
    wait_time = 10

    while retry_count < max_retries:
        try:
            st.write(f"Attempt {retry_count + 1}: Sending request to Groq API...") 
            with st.spinner("Extracting information..."):  
                response = requests.post(endpoint, headers=headers, json=payload, timeout=timeout)

            # Check for successful response
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0 and "message" in result["choices"][0] and "content" in result["choices"][0]["message"]:
                    st.write("Successfully received response from Groq API.")  
                    return result["choices"][0]["message"]["content"].strip()
                else:
                    st.warning("Unexpected response format. Please verify with Groq documentation.")
                    return None

            # Handle rate limiting
            elif response.status_code == 429:
                st.warning(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)  
                retry_count += 1
                wait_time *= 2 

            # Handle other errors with detailed feedback
            else:
                st.error(f"Error {response.status_code} with payload {payload} at endpoint '{endpoint}': {response.text}")
                break  

        except requests.exceptions.Timeout:
            st.error("Request timed out. Please check your network connection or reduce the payload size.")
            break  

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed with exception: {e}")
            break  

    # If all attempts fail
    st.error("Failed to retrieve data after multiple retries. Please verify endpoint and payload parameters with Groq documentation.")
    return None
