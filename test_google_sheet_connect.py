from googleapiclient.discovery import build

file_name_json='C:/Users/a_des/AppData/Roaming/gcloud/application_default_credentials.json'
# Replace with your downloaded JSON credential file path
gc = build.service_account(filename=file_name_json)
url = 'https://docs.google.com/spreadsheets/d/'
response = gc.request('get', url)
print(response.text)  # This will print the raw response
exit
# Spreadsheet ID (found in the URL after "spreadsheets/d/")
#SPREADSHEET_ID = 'https://docs.google.com/spreadsheets/d/1tsOOeG7WHe4jK4LPJPg93mZ7UdkM4wzX5aATgHTYLiM/edit#gid=1145470853'  # You can add multiple sheet IDs to a list
spreadsheet_id = '1tsOOeG7WHe4jK4LPJPg93mZ7UdkM4wzX5aATgHTYLiM/edit#gid=1145470853'  # You can add multiple sheet IDs to a list

# Open the spreadsheet
sheet = gc.open_by_key(spreadsheet_id).bikeshare_stations



# Get data from a specific range (e.g., A1:C5)
#data = sheet.get_all_values()('A1:C5')  # Adjust range as needed - -temp

# Print the data
print(data)