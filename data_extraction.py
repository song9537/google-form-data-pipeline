import os
import json
import re
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


# Define a function to format the data
def format_data(rows):
    formatted_data = []

    for row in rows[1:]:  # Skip the header row (first row)
        timestamp = row[0].split(" ")[0]  # Extract just the date (removing the time)
        names_column = row[1]

        # Use regex to find all names (ignoring numbers in parentheses)
        names = re.findall(r"[\uAC00-\uD7A3]+", names_column)

        # Prepend the timestamp to the list of names
        formatted_row = [timestamp] + names
        formatted_data.append(formatted_row)

    return formatted_data


def data_extraction(id_key):

    # Extract data from google form
    extracted_data = google_extract_value(id_key)

    # Format the fetched data
    formatted_data = format_data(extracted_data)

    return formatted_data
