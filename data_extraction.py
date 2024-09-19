import os
import json
import google.auth
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def google_extract_value(id_key):

    # Path to the service account JSON key file
    SERVICE_ACCOUNT_FILE = "project_key.json"

    # The ID of your Google Sheet (this is in the URL of your sheet)
    SPREADSHEET_ID = id_key

    # The range of the data you want to fetch from the sheet
    RANGE_NAME = "Form Responses 1!A1:D10"

    # Create credentials using the service account key file
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
    )

    # Build the Sheets API service
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API to fetch data
    sheet = service.spreadsheets()
    result = (
        sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    )
    values = result.get("values", [])

    return values


def data_extraction(id_key):

    # Extract data from google form
    extracted_data = google_extract_value(id_key)

    return extracted_data
