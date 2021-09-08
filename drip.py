import gspread

""" Obtains data from the spreadsheet """


def retrieve_data(spreadsheet_object, index):
    worksheet = spreadsheet_object.worksheets()
    return worksheet[index].get_all_values()


""" Sort out the campaigns with the templates """


def campaign(campaign_data, template_data):
    print(campaign_data)

    # Turn list of list into list dictionary for each email template
    flat_template_data = [item for sublist in template_data for item in sublist]
    iteration = iter(flat_template_data)
    templates = dict(zip(iteration, iteration))

    print(dict(zip(iteration, iteration)))


def main():
    # Authenticate the service account using jwt stored in drip-config.py
    gc = gspread.service_account(filename="drip-config.json")

    # Index the spreadsheet with the name
    sh = gc.open("Python of Drip Config (UWA 3)")

    # [CONTACTS, CAMPAIGNS, TEMPLATES, ALL, ProUser, Support, UNSUBSCRIBE, LOG, Emails]
    # Retrieve all data

    campaign_data = retrieve_data(sh, 1)
    template_data = retrieve_data(sh, 2)

    campaign(campaign_data, template_data)


if __name__ == "__main__":
    main()
