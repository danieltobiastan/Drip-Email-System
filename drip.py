import gspread
import numpy
from entity import People, Campaign

# import sendemail

""" Obtains data from the spreadsheet """


def retrieve_data(spreadsheet_object, types):
    worksheet = spreadsheet_object.worksheets()
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


""" Sort the campaigns with the templates """


def campaign(campaign_data, template_data):
    print(campaign_data)

    # Turn list of list into  dictionary for each email template
    flat_template_data = [item for sublist in template_data for item in sublist]
    iteration = iter(flat_template_data)
    templates = dict(zip(iteration, iteration))

    print(templates)


""" Sort the people with the campaigns, organisation, roles, names and emails """


def people(all_people, extra_campaigns_list):
    pass
    # print(all_people)


def main():
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

    # Create people object
    for i in range(len(all_people)):
        all_people[i] = People(
            all_people[i][0], all_people[i][1], all_people[i][2], all_people[i][3], all_people[i][4], all_people[i][5]
        )

    # Create new campaigns
    array_of_campaigns = []
    for i in range(number_of_campaigns):
        array_of_campaigns.append(Campaign(name_of_campaigns[i]))

    # convert the list of list into numpy array for better indexing and less memory usage
    all_people = numpy.array(all_people)

    # campaign(campaign_data, template_data)


if __name__ == "__main__":
    main()
