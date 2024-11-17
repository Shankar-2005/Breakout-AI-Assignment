from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd

def authenticate_google_sheets():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = service_account.Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
    service = build("sheets", "v4", credentials=creds)
    return service

def load_google_sheet(service, sheet_id, range_name):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    values = result.get("values", [])
    return pd.DataFrame(values[1:], columns=values[0])

def update_google_sheet(service, sheet_id, range_name, data):
    body = {
        "values": [data.columns.tolist()] + data.values.tolist()
    }
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()
