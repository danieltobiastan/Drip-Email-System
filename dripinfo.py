import gspread
import asyncio
import numpy as np
import os
import pytz
from dotenv import load_dotenv
from timeit import default_timer as timer
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError
from google.oauth2 import service_account
import pandas as pd

def retrieve_data(sso, types: str):
    """
    Obtains data from the spreadsheet based on parameter.

    :param gspread.models.Spreadsheet sso: spread sheet object from gspread.
    :param types: The type of required date in the option of ['name', 'len', ''].
    :return str name: Name of all the possible worksheet.
    :return int length: Total number of sheet available.
    :return list data: The data in the sheet in form of list.

    Version 1.0.0
    """

    worksheet = sso.worksheets()
    length = len(worksheet)
    if types == "name":  # If type is name return list of sheet names
        names = []
        for i in range(length):
            names.append(worksheet[i].title)
        return names
    elif types == "len":  # If type is len return sheet length
        return length
    else:  # Else return the data
        return worksheet[types].get_all_values()

def get_information(camp_data):
    full_list = [] # gives us the important information of people in a campaign in a list
    for person in camp_data:
        full_list.append(person[0:6])
    return(full_list)

def get_all(sh, number_of_campaigns): #might not need this if we are doing camp by camp
    all_campaigns = []
    for i in range(number_of_campaigns):
        people_in_campaign = retrieve_data(sh, i + 5)[1:] #pro user test line below creates the person class! with important information
        all_campaigns.append(get_information(people_in_campaign))
    return(all_campaigns)


def check_subscriptions(full_data): # gets all the subscribed users/ we don't need this function already...
    all_sub = []
    for campaign in full_data:
        subscribers = []
        for person in campaign:
            if person[1] == 'Sub':
                subscribers.append(person[0])
        all_sub.append(subscribers)
    return(all_sub)

# now i want to segregate the campaigns and link them to the relevant templates

def campaign_information(metadata, campaign_data):
    cl, full, tmp = [], [], []
    c = (np.array(metadata).transpose()[1:]).tolist()
    for i in range(0,len(c),2):
        cl.append(c[i])
    lns = np.array(campaign_data)[:21].transpose()[1:].tolist() # cut the first 21 rows for testing IMPORTANT!!! remove after
    for j in range(0,len(lns),2):
        cpn = []
        td = list(filter(None, lns[j]))
        time = list(filter(None, lns[j+1]))
        for k in range(len(td)):
            item = []
            id, days = td[k], time[k]
            item.append(id)
            item.append(days)
            cpn.append(item)
        tmp.append(cpn)
    for x in range(len(cl)):
        all = []
        all.append(cl[x])
        all.append(tmp[x])
        full.append(all)
    return(full)


def set_default_timing(campaign_drips):
    # if no timing inputs, set to 10am
    for i in range(len(campaign_drips)):
        for j in range(len(campaign_drips[i][1])):
            if ',' in campaign_drips[i][1][j][1]:
                continue
            elif campaign_drips[i][1][j][1] == '0':
                continue
            else:
                campaign_drips[i][1][j][1] = str(campaign_drips[i][1][j][1] + ', 10am')
    return (campaign_drips)

def tag_campaigns(name_of_campaigns, all_data):
    #return a list containing (name of campaign, list of people)
    big_list = []
    for sheetno in range(len(name_of_campaigns)):
        cpns = []
        cpns.append(name_of_campaigns[sheetno])
        cpns.append(all_data[sheetno])
        big_list.append(cpns)
    return(big_list)


def to_hours(timestring): # user should initialise on day 0.
    ts = timestring.split(',')
    if ts[1][-4:] == '12am':
        return ((int(ts[0])) * 24)
    elif ts[1][-4:] == '12pm':
        return ((int(ts[0])) * 24 + 12)
    elif ts[1][-2:] == 'am':
        return ((int(ts[0])) * 24 + int(ts[1][:-2].strip()))
    elif ts[1][-2:] == 'pm':
        return ((int(ts[0])) * 24 + int(ts[1][:-2].strip()) + 12)

def initialising(dummy_information, dummy_campaign):
    current_date = np.datetime64(np.datetime64(datetime.now()), 'h')
    campaign = []
    campaign.append(dummy_campaign[0][0])
    # for each campaign,
    for drip in dummy_campaign[1][1:]:
        drip_list, emails = [], []
        temp_id, time_todrip = drip[0], to_hours(drip[1])
        drip_list.append(temp_id)
        for persons in dummy_information[1]:
            initialise_date = pd.to_datetime(str(persons[0])).strftime('%Y-%d-%m')
            date_from_joined = (current_date - np.datetime64(initialise_date, 'h')).astype(int)
            if date_from_joined == time_todrip:
                emails.append(persons[1])
        if len(emails) == 0:
            continue
        else:
            drip_list.append(emails)
        campaign.append(drip_list)
    return(campaign)


def main():
    gc = gspread.service_account(filename="drip-config.json")
    sh = gc.open("Python of Drip Config (UWA 3)")

    number_of_campaigns = retrieve_data(sh, "len") - 5  # i have the number of campaigns here i need this for later
    name_of_campaigns = retrieve_data(sh, "name")[5:]  # names of campaigns here in a list
    campaign_metadata = retrieve_data(sh, 1)[:3]
    campaign_data = retrieve_data(sh, 1)[4:]  # this is a bit weird might come together later

    all_campaign_users = get_all(sh, number_of_campaigns)
    all_campaign_information = (campaign_information(campaign_metadata, campaign_data))
    tagged_contacts = (tag_campaigns(name_of_campaigns, all_campaign_users))
    tagged_drips = set_default_timing(all_campaign_information)
    batch = []
    for name in range(len(tagged_drips)):
        for camp in tagged_contacts:
            if tagged_drips[name][0][1] == camp[0]:
                cent = []
                cent.append(tagged_drips[name][0])
                sf = initialising(camp,tagged_drips[name])
                cent.append(sf)
                batch.append(cent)
    return batch

#call the main function.... check the last campaign and ensure times and contacts tally!
# first item in main = [Campaign name, contact list, sender]
# second item in main = [contact list, list of lists of the templateid and emails]
# a few conditions: make sure campaigns sheet structure is 2 cols, sheet names should be contact list names in cpgns, runs hourly
## see line 71, currently capped to first 21 drips because of the big yellow note on campaigns tab...
print(main()[-1])