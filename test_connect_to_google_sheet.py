#from google-api-python-client import build
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
#from google.oauth2 import service_account
from google.cloud import bigquery

# Replace with your Google Sheet ID(s)
SPREADSHEET_ID = 'https://docs.google.com/spreadsheets/d/1tsOOeG7WHe4jK4LPJPg93mZ7UdkM4wzX5aATgHTYLiM/edit#gid=1145470853'  # You can add multiple sheet IDs to a list
#SPREADSHEET_ID = '1145470853'  # You can add multiple sheet IDs to a list
# Replace with the path to your Google Cloud Service Account JSON key file
#SERVICE_ACCOUNT_FILE = 'C:/Users/a_des/OneDrive/Documents/Python development/biqguery_key_credentials_test.json'
SERVICE_ACCOUNT_FILE = 'C:/Users/a_des/AppData/Roaming/gcloud/application_default_credentials.json'

# Replace with your BigQuery project ID and dataset ID
PROJECT_ID = 'gleaming-mason-268619'
DATASET_ID = 'austin_bikeshare'

def extract_from_sheets(sheet_id):
  """Extracts data from a Google Sheet."""
   #sheets = sheet_metadata.get('sheets', '')  # Handle no sheets case
  #gc = build('bikeshare_stations', 'v4', credentials=MY_CREDENTIALS)  # Use appropriate authentication
  gc = build('sheets', 'v4')  # Use appropriate authentication
  worksheet = gc.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range='Sheet1!A1:Z').execute()  # Adjust range as needed
  values = worksheet.get('values', [])
  return values

#sheets = sheet_metadata.get('sheets', '')  # Handle no sheets case

# Find the sheet ID for the "bikeshare_stations" tab

# Extract data from Google Sheets
sheet_data = []
for sheet_id in SPREADSHEET_ID:
  sheet_data.extend(extract_from_sheets(sheet_id))

# Load data to BigQuery table (replace with your desired table name)
#load_to_bigquery(sheet_data, 'your_table_name')

print("Data loaded successfully!")