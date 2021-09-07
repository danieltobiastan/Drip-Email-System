import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('drip-config.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Python of Drip Config (UWA 3)").sheet1

# Extract and print first row of the values
list_of_hashes = sheet.row_values(1)
print(list_of_hashes)

#update a cell
sheet.update_cell(6, 2, "Daniel")
sheet.update_cell(6, 3, "Tan")
sheet.update_cell(6, 4, "UWA")
sheet.update_cell(6, 5, "Creator")
list_of_hashes = sheet.row_values(6)
print(list_of_hashes)