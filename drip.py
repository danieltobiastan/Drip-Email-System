import gspread
import numpy as np
from entity import People, Campaign
# from timeit import default_timer as timer

# import send_email

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
    print(type(sso))
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
        people_in_campaign = [
            People(person[0], person[1], person[2], person[3], person[4], person[5]) for person in people_in_campaign
        ]
        array_of_campaigns[i].add_people(people_in_campaign)

    return array_of_campaigns


"""
# TODO

- Find a solution to sort out the campaign page after the client meeting
- Create an AppScript function to add timestamp as soon as Ramon adds the email
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
    campaign_data = retrieve_data(sh, 1)
    template_data = retrieve_data(sh, 2)
    all_people = retrieve_data(sh, 5)[1:]  # read everything after row 1

    array_of_campaigns = campaigns(sh, name_of_campaigns, number_of_campaigns)

    template(template_data)

    # end = timer()
    # print("it takes " + str((end - start)) + " seconds")


if __name__ == "__main__":
    main()
