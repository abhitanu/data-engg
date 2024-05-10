from googleapiclient.discovery import build
from google.cloud import bigquery
import os

# Define the spreadsheet ID (portion after the /d)
#spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1tsOOeG7WHe4jK4LPJPg93mZ7UdkM4wzX5aATgHTYLiM/edit#gid=1284962629'
developer_key='AIzaSyDwYDynHvCPCHV3xnCtRHCjltCE918dFdg' # This is a API key
spreadsheet_id = '1tsOOeG7WHe4jK4LPJPg93mZ7UdkM4wzX5aATgHTYLiM' # See above URL. Its after the "/d" upto the next "/"
tab_name = 'sheet4'
sheet_range = f"{tab_name}!A2:C5"

# The first 2 params do not represent the sheet (so hard coded and dont need to change)
service = build('sheets', 'v4', developerKey=developer_key) # We are using API Key here (not credemtials file)

# Interact with the Sheet
sheet = service.spreadsheets() # returns an object representing the Google Sheets service
result = sheet.values().get(spreadsheetId=spreadsheet_id, range=sheet_range).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print('Data:')
    for row in values:
        print(row)

## We were able to load the data from the google sheet.

credentials_file = 'C:/Users/a_des/OneDrive/Documents/Python development/biqguery_key_credentials_test.json'

# Check if the file exists
if not os.path.exists(credentials_file):
    raise ValueError(f"The file '{credentials_file}' does not exist.")
else:
    print ('All good')



bq_client = bigquery.Client.from_service_account_json(credentials_file)
DATASET_ID='gleaming-mason-268619.testdb_write_from_sheet'
table_name='my_test_sheet_data'

table_ref = bq_client.dataset(DATASET_ID).table(table_name)
table = bq_client.get_table(table_ref)
"""
# Define your list of data

errors = bq_client.insert_rows(table_ref, values, selected_fields=[bigquery.SchemaField('col1', 'INTEGER'), bigquery.SchemaField('col2', 'INTEGER'), bigquery.SchemaField('col3', 'INTEGER')])  # API request
if errors == []:
    print('Data inserted successfully.')
else:
    print('Encountered errors while inserting data:', errors)
"""