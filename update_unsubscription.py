import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

url = "https://api.sendgrid.com/v3/suppression/unsubscribes"

payload = "{}"

headers = {
    # 'authorization': "Bearer api_key(need change for testing)"
    'authorization': "Bearer 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",
    'content-type': "application/json"
    }

response = requests.request("GET", url, data=payload, headers=headers)

unsub_users = json.loads(response.text)
unsub_emails = [user_info['email'] for user_info in unsub_users]

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/black/Desktop/drip-config.json', scope)
client = gspread.authorize(creds)

# get json key from github
#drip_cfg_resp = requests.get('https://raw.githubusercontent.com/Extrosoph/Drip-Email-System/python/drip-config.json')
#creds_dict = drip_cfg_resp.json()
#credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
#client = gspread.authorize(credentials)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Python of Drip Config (UWA 3)").sheet1

next_row = len(sheet.get_all_values()) + 1

for k in range(1, next_row):
    row = sheet.row_values(k)       # Read a whole row
    if row[1] in unsub_emails:      # column 1 stores email
        sheet.update_cell(k, 12, "Unsubscribed")    # Column 12 stores subscription status