import numpy as np


class People:
    """
    This class deals with the people`s details such as name, emails, date joined, organisation etc.

    Version 1.0.0.
    """

    def __init__(
        self, date_joined: str, email: str, first_name: str, last_name: str, organisation: str, role: str, tag: str
    ):
        """
        Constructor method to create each person.

        :param date_joined: The date each person joins the drip system.
        :param email: The email of each person.
        :param first_name: The first name of the person.
        :param last_name: The last name of the person.
        :param organisation: The organisation the person belongs in.
        :param role: the role of the person.
        :param tag: The tag attribute of the person.
        """

        self.date_joined = date_joined
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.organisation = organisation
        self.role = role
        self.tag = tag
        self.email_tracker = ""
        self.time = ""

    def get_fullname(self):
        """
        Get the full name of the person in the format of firstname lastname.

        :return name str: The full name of the person.
        """

        return self.first_name + " " + self.last_name

    def get_date_joined(self):
        """
        Get the date the person joined.

        :return date_joined str: The date the person joined.
        """

        return self.date_joined

    def get_email(self):
        """
        Get the person`s email.

        :return email str: The email of the person.
        """
        return self.email

    def get_organisation(self):
        """
        Get the organisation of the person.

        :return organisation str: The organisation of the person.
        """

        return self.organisation

    def get_role(self):
        """
        Get the person`s role.

        :return role str: The person`s role.
        """

        return self.role

    def get_tag(self):
        """
        Get person`s tag.

        :return tag str: The person`s tag.
        """

        return self.tag

    def get_tracker(self):
        """
        Get person`s tracker to check the next date to send email.

        :return email_tracker str: The next date for email to be sent.
        """
        return self.email_tracker

    def read_tracker(self, date: str):
        """
        Set the person`s tracker from google sheet if already placed after welcome.

        :param date: The date in the string format yyyy/mm/dd.
        """

        if date != "":
            self.email_tracker = np.datetime64(date)
        else:
            self.email_tracker = date

    def set_tracker(self, date: str, time: str):
        """
        Set person`s tracker from main drip function to google sheet and convert from using am/pm to 24hr time.

        :param date: The date added in the format of yyyy/mm/dd.
        :param time: The time for each person in the format of 10am/pm.
        """
        if time == "":
            self.email_tracker = date + np.timedelta64(10, "h")
        else:
            if "am" in time:
                self.email_tracker = date + np.timedelta64(int(time[:2]), "h")
            else:
                self.email_tracker = date + np.timedelta64(int(time[:1]) + 12, "h")


class Campaign:
    """
    This class deals with the the different campaigns and their specific attribute such name and list of people.

    Version 1.0.0
    """

    def __init__(self, name: str):
        """
        The constructor to make a campaign object.

        :param name: The name of the campaign
        """

        self.name = name
        self.people = []

    def get_people(self):
        """
        Get the list of people in the campaign

        :return people list: List of people in campaign.
        """

        return self.people

    def get_name(self):
        """
        Get the name of the campaign

        :return name str: The name of the campaign.
        """

        return self.name

    def add_people(self, list_of_people):
        """
        Add people in the campaign.

        :param list_of_people list/str: The list of people to be in the campaign.
        """

        if type(list_of_people) is list:
            self.people.extend(list_of_people)
        else:
            self.people.append(list_of_people)

    def remove_people(self, list_of_people):
        """
        Remove people from the campaign.

        :param list_of_people list/str: The list of people be removed from campaign.
        """
        if type(list_of_people) is list:
            for person in list_of_people:
                self.people.remove(person)
        else:
            self.people.remove(list_of_people)


class Email:
    """
    This class deals with the email batches object.

    Version 1.0.0
    """

    def __init__(
        self, email_from: str, email_to: list, time_to_send: np.datetime64, subject: str, template: str, campaign: str
    ):
        """
        The constructor for the email batches.

        :param email_from: The sender`s email address.
        :param email_to: The list of people to send to.
        :param time_to_send: The time to send the emails.
        :param subject: The subject of the email.
        :param template: The email templates to send to SendGrid.
        :param campaign: The campaign name of the people.
        """
        self.email_to = email_to
        self.email_from = email_from
        self.time_to_send = time_to_send
        self.subject = subject
        self.template = template
        self.campaign = campaign

    def get_email_to(self):
        """
        Get the list of email`s receiver.

        :return email_to list: The list of receiver.
        """
        return self.email_to

    def get_email_from(self):
        """
        Get the sender`s email address.

        :return email_from str: The sender`s address.
        """
        return self.email_from

    def get_time_to_send(self):
        """
        Get the time to send in a numpy datetime format yyyy/mm/dd/HH.

        :return time_to_send numpy.datetime64: The time for the email to be sent.
        """
        return self.time_to_send

    def get_subject(self):
        """
        Get the subject of the email.

        :return subject str: The subject of the email.
        """
        return self.subject

    def get_template(self):
        """
        Get the template of the email.

        :return template str: The email`s template.
        """
        return self.template

    def get_campaign(self):
        """
        Get the campaign name.

        :return campaign str: The campaign`s name.
        """
        return self.campaign


"""" Testing functionality with dummy data """
# person1 = People("aixxmtg@charter.gov", "Paul", "Beal", "Twillio", "CEO", "Support")
# person2 = People("h98@comcast.net", "Mary", "Fitz", "Curtin University", "researcher", "Pro")
# person3 = People("22764884@student.uwa.edu.au", "Sam", "Tink", "Google", "CFO", "Support")
#
# person4 = People("h98@comcast.net", "Mary", "Fitz", "Curtin University", "researcher", "Pro")
# person5 = People("22764884@student.uwa.edu.au", "Sam", "Tink", "Google", "CFO", "Support")
#
#
# pro = [person1, person2, person3, person4, person5]
# pro.remove(person4)
# people2 = [person4]
# people3 = [person5]
# people = [
#     person1,
#     person2,
#     person3,
# ]
#
# print(person1.get_fullname())
# pro_campaigns = Campaign("Pro")
# pro_campaigns.add_people(people)
# pro_campaigns.add_people(people2)
# pro_campaigns.add_people(people3)
#
# # print(pro_campaigns.get_people())
# pro_people = pro_campaigns.get_people()
#
# pro_campaigns.remove_people(person4)
# # print(pro_campaigns.get_people())
