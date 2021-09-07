Drip Email System

Before running the SendGrid, make sure you run this in terminal/powershell first:

Terminal(MacOS): 
echo "export SENDGRID_API_KEY='API_KEY'" > sendgrid.env #change placeholder api key
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env

Windows Powershell:
$Env:SENDGRID_API_KEY = 'API KEY' #change placeholder api key
