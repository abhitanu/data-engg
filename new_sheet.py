from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

# Define the Google Sheets API scope
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

#credentials_file = 'C:/Users/a_des/AppData/Roaming/gcloud/application_default_credentials.json'  # Replace with your file path
credentials_file = 'C:/Users/a_des/OneDrive/Documents/Python development/biqguery_key_credentials_test.json'

try:
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, SCOPES)
    print('Client id :' + credentials.client_id)
    print('token_uri :' + credentials.token_uri)
    #print(credentials.private_key_id)
    #print(credentials.scopes)
except (IOError, KeyError):
    print('Credentials file not found or invalid.')

service = build('sheets', 'v4', developerKey='AIzaSyDwYDynHvCPCHV3xnCtRHCjltCE918dFdg') # We are using API Key here (not credemtials file)

# Define the spreadsheet ID and range
#spreadsheet_id = 'https://docs.google.com/spreadsheets/d/1tsOOeG7WHe4jK4LPJPg93mZ7UdkM4wzX5aATgHTYLiM/edit#gid=1284962629'
spreadsheet_id = '1tsOOeG7WHe4jK4LPJPg93mZ7UdkM4wzX5aATgHTYLiM'

tab_name = 'sheet4'
sheet_range = f"{tab_name}!A1:C5"  # Adjust the range as needed (e.g., B2:D7)

# Interact with the Sheet
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=spreadsheet_id, range=sheet_range).execute()
values = result.get('values', [])

if not values:
    print('No data found...starting in github')
else:
    print('Data:')
    for row in values:
        print(row)