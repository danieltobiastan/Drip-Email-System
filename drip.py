import gspread
import numpy as np
from entity import People, Campaign
import send_email

# from timeit import default_timer as timer


""" 
Obtains data from the spreadsheet based on parameter

:param gspread.models.Spreadsheet sso: spread sheet object from gspread
:param types: the required data

* Not sure how to do different returns comments
:return
- types = 'name' : name of all the possible worksheet
- types = 'len' : total number of worksheets
- types = 'index of sheet' : all the data of that sheet in list
"""


def retrieve_data(sso, types):
    worksheet = sso.worksheets()
    length = len(worksheet)
    if types == "name":  # If type is name return list of sheet names
        names = []
        for i in range(length - 1):
            names.append(worksheet[i].title)
        return names
    elif types == "len":  # If type is len return sheet length
        return length - 1
    else:  # Else return the data
        return worksheet[types].get_all_values()


""" 
Sort the templates and returns a dictionary

:param str template_data: the data read from sheet
:return dict templates: the dictionary in the form of {template name: sendGrid template id}
"""


def template(template_data):
    # Turn list of list into  dictionary for each email template
    flat_template_data = [item for sublist in template_data for item in sublist]
    iteration = iter(flat_template_data)
    templates = dict(zip(iteration, iteration))
    return templates


"""
Convert the date format from dd/mm/yyyy to yyyy/mm/dd for numpy datetime64()

:param str date: date from sheet
:return np.datetime64 day: date in datetime64 format
"""


def date_format(date):
    date = date.replace("/", "-")
    date = date.split("-")
    date.reverse()
    day = ""
    for i in range(len(date)):
        if i == len(date) - 1:
            day += str(date[i])
        else:
            day += str(date[i]) + "-"
    return np.datetime64(day)


""" 
Create new campaigns also using list comprehension and placing then into numpy array

:param gspread.worksheet sh: spreadsheet to read
:param str names: the name of the campaign in string
:param int number: the number of campaigns to make
:return numpy.ndarray array_of_campaigns : list of campaigns and the people

"""


def campaigns(sh, names, number):
    # Create new campaigns also using list comprehension and placing then into numpy array
    array_of_campaigns = np.array([Campaign(name) for name in names])
    for i in range(number):
        people_in_campaign = retrieve_data(sh, i + 5)[1:]
        print(date_format(people_in_campaign[0][0]))
        people_in_campaign = [
            People(date_format(person[0]), person[1], person[2], person[3], person[4], person[5], person[6], person[7])
            for person in people_in_campaign
        ]
        array_of_campaigns[i].add_people(people_in_campaign)

    return array_of_campaigns


"""
Set the next date for the emails to be sent in the campaign list

:param Campaign campaign: campaign object that holds the people objects
:param str next_day: next date for emails to be sent 
"""


def next_email_date(campaign, next_day):
    if "," in next_day:
        day, time = next_day.split(",")
        time = time.strip()
        next_day = np.timedelta64(int(day), "D")
        for person in campaign.get_people():
            person.set_tracker(person.get_date_joined() + next_day, time)
    else:
        next_day = np.timedelta64(int(next_day), "D")
        for person in campaign.get_people():
            person.set_tracker(person.get_date_joined() + next_day, "")


"""
# TODO

- Find a solution to sort out the campaign page after the client meeting
- Add a way to check when the next email is to be sent and if it is empty then send them the welcome email
- Add a way to write data to log as soon as emails are sent
"""


def main():
    # start = timer()
    # Authenticate the service account using jwt stored in drip-config.py
    gc = gspread.service_account(filename="drip-config.json")

    # Index the spreadsheet with the name
    sh = gc.open("Python of Drip Config (UWA 3)")

    # [CONTACTS, CAMPAIGNS, TEMPLATES, UNSUBSCRIBE, LOG, ALL, ProUser, Support, Emails]
    # Retrieve all data

    number_of_campaigns = retrieve_data(sh, "len") - 5  # because 5 sheets are constant
    name_of_campaigns = retrieve_data(sh, "name")[5:]
    campaign_metadata = retrieve_data(sh, 1)[:3]
    campaign_data = retrieve_data(sh, 1)[3:]
    template_data = retrieve_data(sh, 2)
    all_people = retrieve_data(sh, 5)[1:]  # read everything after row 1

    # print(campaign_metadata)
    campaign_array = np.array(campaign_data).transpose()
    # print(campaign_array)

    # print(campaign_array[2])
    array_of_campaigns = campaigns(sh, name_of_campaigns, number_of_campaigns)
    template_dict = template(template_data)
    # print(template_dict)

    email_to = []
    email_templates = []
    # For each campaign sort the next email date for each person
    for person in array_of_campaigns[0].get_people():
        if person.get_tracker() == "":
            email_to.append(person.get_email())

    # send welcome
    email_template = template_dict.get(campaign_array[1][1])
    subject = campaign_array[1][1]
    # send_email(email_to, email_template, subject)

    # add to log

    # set the date for next email
    # print(campaign_array[2][2])
    next_email_date(array_of_campaigns[0], campaign_array[2][2])

    # get the sheet
    # write the tracker date into the sheet

    # end = timer()
    # print("it takes " + str((end - start)) + " seconds")


if __name__ == "__main__":
    main()
