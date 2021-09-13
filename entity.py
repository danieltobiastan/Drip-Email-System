""" People class to store information about each person """
import numpy as np


class People:
    def __init__(self, email, first_name, last_name, organisation, role, tag):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.organisation = organisation
        self.role = role
        self.tag = tag
        self.date = np.datetime64('now')

    def get_fullname(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.email

    def get_organisation(self):
        return self.organisation

    def get_role(self):
        return self.role

    def get_tag(self):
        return self.tag

    def get_date(self):
        return self.date


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
