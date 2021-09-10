import gspread
import numpy
from entity import People, Campaign
#import sendemail

""" Obtains data from the spreadsheet """


def retrieve_data(spreadsheet_object, index):
    worksheet = spreadsheet_object.worksheets()
    return worksheet[index].get_all_values()


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

    # [CONTACTS, CAMPAIGNS, TEMPLATES, ALL, ProUser, Support, UNSUBSCRIBE, LOG, Emails]
    # Retrieve all data

    campaign_data = retrieve_data(sh, 1)
    template_data = retrieve_data(sh, 2)
    all_people = retrieve_data(sh, 3)

    # convert the list of list into numpy array for better indexing and less memory usage
    all_people = numpy.array([numpy.array(person) for person in all_people])

    print(all_people)
    campaign(campaign_data, template_data)


if __name__ == "__main__":
    main()
