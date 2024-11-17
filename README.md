# Breakout-AI-Assignment
## AI Agent Dashboard

### Project Overview

The **AI Agent Dashboard** is designed to automate information retrieval for entities listed in a dataset. This application allows users to upload a CSV file or connect to a Google Sheet, specify custom prompts, and utilize web search and LLM capabilities to extract structured information for each entity. The project integrates APIs, including OpenAI and SerpAPI, and provides options for outputting results in a downloadable format or updating a Google Sheet.

### Key Features and Expected Outcomes

This project fulfills the following functionalities:

#### 1. File Upload and Google Sheets Connection  
   - **Goal**: Allow users to upload a CSV file or connect to a Google Sheet.
   - **Outcome**: 
     - Users can upload a CSV or connect Google Sheets by entering credentials.
     - Display columns for selection, including a data preview.
   - **Technical Details**: Integrated with Google Sheets API for real-time access, allowing users to authenticate and pull data directly.

#### 2. Dynamic Query Input with Prompt Template  
   - **Goal**: Enable custom prompts with placeholders for entity-based searches.
   - **Outcome**: 
     - A prompt input box where users can define queries such as “Get email of {company}.”
     - Clear preview of generated queries based on the template.
  
#### 3. Automated Web Search for Information Retrieval  
   - **Goal**: Perform web searches using the custom prompt to gather relevant data.
   - **Outcome**:
     - For each entity in the selected column, the agent conducts a web search.
     - API integration with SerpAPI to handle searches with rate-limiting and response management.
   - **Technical Details**: Includes error handling for rate limits and quota errors.
   
#### 4. LLM Integration for Parsing and Extraction  
   - **Goal**: Use OpenAI's API to extract specific information based on search results.
   - **Outcome**:
     - Sends search results to OpenAI’s API with an entity-specific prompt to extract the needed information.
   - **Technical Details**: Handles `RateLimitError` by retrying with delays, up to three times.

#### 5. Display and Export Results  
   - **Goal**: Provide extracted information in a user-friendly table with download options.
   - **Outcome**:
     - Display results within the app, organized by entity and extracted data.
     - Downloadable as CSV or optional update to Google Sheets.
   - **Technical Details**: Option for “Download CSV” and Google Sheets update.

#### 6. Advanced Features  
   - **Error Handling**: Integrated retries and user notifications for failed queries.
   - **Batch Processing**: For large datasets, limits the number of entities processed to avoid rate limits and API quota issues.
   - **API Key Instructions**: Clear guidance on entering API keys securely in the app sidebar.

---

### Technology Stack
- **Dashboard/UI**: Streamlit
- **Data Handling**: Pandas for CSV files; Google Sheets API for Google Sheets integration
- **Search API**: SerpAPI (or ScraperAPI)
- **LLM API**: OpenAI’s GPT API
- **Backend**: Python
- **Agent Framework**: LangChain (optional, for more advanced agent management)

---

### Setup Instructions

#### Prerequisites
1. **Python 3.7 or higher** is recommended.
2. **Install Dependencies**:
   - Clone the repository and navigate to the project folder.
   - Run:
     ```bash
     pip install -r requirements.txt
     ```

3. **API Keys and Environment Variables**:
   - Ensure you have the following API keys:
     - **OpenAI API Key**: [Sign up and get the key here](https://platform.openai.com/signup).
     - **SerpAPI Key**: [Sign up and get the key here](https://serpapi.com/).
   - **Google Sheets Credentials**:
     - Save your `credentials.json` file from Google Cloud Console in the root directory.
     - Enable the Google Sheets API and share the sheet with the service account email provided in the credentials.

#### Running the Application
1. **Start Streamlit**:
   ```bash
   streamlit run app.py
