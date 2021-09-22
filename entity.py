import numpy as np


""" People class to store information about each person """


class People:
    def __init__(self, date_joined, email, first_name, last_name, organisation, role, tag, email_tracker):
        self.date_joined = date_joined
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.organisation = organisation
        self.role = role
        self.tag = tag
        self.email_tracker = email_tracker
        self.time = ''
        self.next_template = ''

    def get_fullname(self):
        return self.first_name + " " + self.last_name

    def get_date_joined(self):
        return self.date_joined

    def get_email(self):
        return self.email

    def get_organisation(self):
        return self.organisation

    def get_role(self):
        return self.role

    def get_tag(self):
        return self.tag

    def get_tracker(self):
        return self.email_tracker

    def get_next_template(self):
        return self.next_template

    def set_tracker(self, date, time):
        if time == "":
            self.email_tracker = date + np.timedelta64(10, "h")
        else:
            if "am" in time:
                self.email_tracker = date + np.timedelta64(int(time[:2]), "h")
            else:
                self.email_tracker = date + np.timedelta64(int(time[:1]) + 12, "h")

    def set_next_template(self, template):
        self.next_template = template


""" Campaign class to store information about each campaign """


class Campaign:
    def __init__(self, name):
        self.name = name
        self.people = []

    def get_people(self):
        return self.people

    def get_name(self):
        return self.name

    def add_people(self, list_of_people):
        if type(list_of_people) is list:
            self.people.extend(list_of_people)
        else:
            self.people.append(list_of_people)

    def remove_people(self, list_of_people):
        if type(list_of_people) is list:
            for person in list_of_people:
                self.people.remove(person)
        else:
            self.people.remove(list_of_people)


class Email:
    def __init__(self, email_from, email_to, time_to_send):
        self.email_to = email_to
        self.email_from = email_from
        self.time_to_send = time_to_send


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
