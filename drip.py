import gspread
import numpy
from entity import People, Campaign
#import sendemail

""" Obtains data from the spreadsheet """


def retrieve_data(spreadsheet_object, types):
    worksheet = spreadsheet_object.worksheets()
    if types == 'name':                                 # If type is name return list of sheet names
        return worksheet
    elif types == 'len':                                # If type is len return sheet length
        return len(worksheet) - 1
    else:                                               # Else return the data
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

    number_of_campaigns = retrieve_data(sh, 'len') - 5              # because 5 sheets are not changed
    name_of_campaigns = retrieve_data(sh, 'name')[5:]               # need to fix this to just get name
    campaign_data = retrieve_data(sh, 1)
    template_data = retrieve_data(sh, 2)
    all_people = retrieve_data(sh, 5)

    for i in range(len(all_people)):
        all_people[i] = People(all_people[0], all_people[1], all_people[2], all_people[3], all_people[4], all_people[5])

    # Create new campaigns
    list_of_campaigns = [None] * number_of_campaigns
    for i in range(len(list_of_campaigns)):
        list_of_campaigns[i] = Campaign(name_of_campaigns[i])

    print(list_of_campaigns[0].get_name())

    # convert the list of list into numpy array for better indexing and less memory usage
    all_people = numpy.array([numpy.array(person) for person in all_people])


    campaign(campaign_data, template_data)


if __name__ == "__main__":
    main()
