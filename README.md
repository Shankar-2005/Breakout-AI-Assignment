# Breakout-AI-Assignment
## AI Agent Dashboard

### Project Overview

The **AI Agent Dashboard** automates information retrieval for entities listed in a dataset. This application allows users to upload a CSV file or connect to a Google Sheet, specify custom prompts, and utilize web search and LLM capabilities to extract structured information for each entity. The project integrates the Groq API for LLM processing and SerpAPI for web search, with options to download results or update a Google Sheet.

---

### Key Features

- **File Upload or Google Sheets Connection**: Choose between uploading a CSV file or using a Google Sheet as the data source.
- **Custom Query Prompt**: Specify custom prompts to search for information relevant to each entity.
- **Automated Web Search**: Uses SerpAPI to gather search results for each entity.
- **LLM-based Information Extraction**: Groq’s API processes the search results and extracts structured information.
- **Results Download**: Download the extracted data as a CSV file or update a Google Sheet.

---

### Technology Stack
- **UI Framework**: Streamlit
- **Data Handling**: Pandas for CSV files; Google Sheets API for Google Sheets integration
- **Search API**: SerpAPI
- **LLM API**: Groq API
- **Backend**: Python

---

### Setup Instructions

#### Prerequisites
1. **Python 3.7 or higher**
2. **API Access**: Ensure you have the necessary API keys for Groq and SerpAPI:
   - **Groq API Key**: Sign up at [Groq's API Platform](https://groq.com) and get an API key.
   - **SerpAPI Key**: Sign up at [SerpAPI](https://serpapi.com/) and obtain your API key.
3. **Google Sheets API** (Optional for Google Sheets integration):
   - Enable the Google Sheets API in the Google Cloud Console.
   - Obtain a `credentials.json` file and place it in the project root directory.

#### Installing Dependencies
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Breakout-AI-Assignment.git
   cd Breakout-AI-Assignment

#### Running the Application
1. **Start Streamlit**:
   ```bash
   streamlit run app.py
