import streamlit as st
import pandas as pd
import time
from search_api import search_entity
from llm_processing import extract_info_with_llm
from google_sheets_integration import authenticate_google_sheets, load_google_sheet, update_google_sheet

# Initialize Streamlit app
st.set_page_config(page_title="AI Agent Dashboard", layout="wide")
st.title("AI Agent Dashboard")

# Sidebar for API keys
st.sidebar.title("Configuration")
serpapi_key = st.sidebar.text_input("SerpAPI Key", type="password")
groq_key = st.sidebar.text_input("Groq API Key", type="password")  # Using Groq API key instead of OpenAI

# Choose Data Input Source
st.subheader("Data Input")
data_source = st.selectbox("Select Data Source", ["Upload CSV", "Google Sheets"])

if data_source == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("CSV Data Preview")
        st.dataframe(data.head())

elif data_source == "Google Sheets":
    service = authenticate_google_sheets()
    sheet_id = st.text_input("Enter Google Sheet ID")
    range_name = st.text_input("Enter Range (e.g., 'Sheet1!A1:D10')")
    if sheet_id and range_name:
        data = load_google_sheet(service, sheet_id, range_name)
        st.write("Google Sheets Data Preview")
        st.dataframe(data.head())

# Prompt and Column Selection
if 'data' in locals():
    entity_column = st.selectbox("Select the column for entities", data.columns)
    prompt_template = st.text_input("Enter custom prompt", "Find email address of {entity}")
    st.write(f"Example Prompt: `{prompt_template.format(entity=data[entity_column].iloc[0])}`")

# Process Data Button
if 'data' in locals() and st.button("Process Data"):
    results = []
    for i, entity in enumerate(data[entity_column]):
        if i > 0:
            time.sleep(1)  # Delay to reduce rate of requests

        # Perform web search and information extraction
        search_results = search_entity(entity, prompt_template, serpapi_key)
        if search_results:
            extraction_prompt = f"Extract the following information for {entity}: {prompt_template}"
            extracted_info = extract_info_with_llm(search_results, extraction_prompt, groq_key)
            results.append({"Entity": entity, "Extracted Info": extracted_info})
        else:
            st.error(f"Failed to retrieve data for {entity}")

    # Display and Export Results
    result_df = pd.DataFrame(results)
    st.write("Extracted Information")
    st.dataframe(result_df)
    csv = result_df.to_csv(index=False)
    st.download_button("Download CSV", csv, "extracted_data.csv", "text/csv")

    # Optional: Update Google Sheet
    if data_source == "Google Sheets" and st.checkbox("Update Google Sheet with Results"):
        update_google_sheet(service, sheet_id, range_name, result_df)
        st.success("Google Sheet successfully updated with extracted data!")
