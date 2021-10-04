import unittest
import numpy as np
from entity import People, Campaign, Email


class test_drip(unittest.TestCase):
    """
    Basic testing for some functions in drip.py file.

    TODO:
        - complete all the functions
        - remove pass after completion of functions
    """

    def setUp(self):
        pass

    def test_date_format_sheet_python(self):
        """
        Basic test to change the date format from dd/mm/yyyy to yyyy-mm-dd.
        """
        pass

    def test_next_email_date(self):
        """
        Basic test to check if the next day is correct.
        """
        pass

    def test_finding_duplicates_dates(self):
        """
        Basic test to check if the number and type of duplicates are correct.
        """
        pass

    def tearDown(self) -> None:
        (self)


class test_people(unittest.TestCase):
    """
    Basic testing for the people`s class.
    """

    def setUp(self):
        # Load test data
        self.person = People("10/10/2021", "randomemail@service.com", "james", "lost", "UWA", "student", "Pro")

    def test_fullname(self):
        """
        Basic test for get_fullname().
        """

        self.assertEqual(self.person.get_fullname(), "james lost")

    def test_date_joined(self):
        """
        Basic test for get_date_joined().
        """

        self.assertEqual(self.person.get_date_joined(), "10/10/2021")

    def test_get_email(self):
        """
        Basic test for get_email().
        """

        self.assertEqual(self.person.get_email(), "randomemail@service.com")

    def test_get_organisation(self):
        """
        Basic test for get_organisation().
        """

        self.assertEqual(self.person.get_organisation(), "UWA")

    def test_get_role(self):
        """
        Basic test for get_role().
        """

        self.assertEqual(self.person.get_role(), "student")

    def test_get_tag(self):
        """
        Basic test for get_tag().
        """

        self.assertEqual(self.person.get_tag(), "Pro")

    def test_get_tracker(self):
        """
        Basic test for get_tracker() without initialising the value.
        """

        self.assertEqual(self.person.get_tracker(), "")

    def test_read_tracker(self):
        """
        Basic test for read_tracker(date) to place a tracker value.
        """

        # Testing with empty string
        self.person.read_tracker("")
        self.assertEqual(self.person.get_tracker(), "")

        # Testing with correct time format
        self.person.read_tracker("2021-10-21")
        self.assertEqual(self.person.get_tracker(), np.datetime64("2021-10-21"))

        # Testing with incorrect time format
        self.assertEqual(self.person.read_tracker("21-10-2021"), "Incorrect date format, must be yyyy-mm-dd")

    def test_set_tracker(self):
        """
        Basic test for set_tracker(date) without initialising the value.
        """

        # Testing missing time inputs
        self.person.set_tracker(np.datetime64("today"), "")
        self.assertEqual(self.person.get_tracker(), np.datetime64("today") + np.timedelta64(10, "h"))

        # Testing missing date inputs
        self.assertEqual(self.person.set_tracker("", "10am"), "Missing date input!")

        # Testing am time
        self.person.set_tracker(np.datetime64("today"), "10am")
        self.assertEqual(self.person.get_tracker(), np.datetime64("today") + np.timedelta64(10, "h"))

        # Testing pm time
        self.person.set_tracker(np.datetime64("today"), "13pm")
        self.assertEqual(self.person.get_tracker(), np.datetime64("today") + np.timedelta64(13, "h"))

    def tearDown(self) -> None:
        (self)


class test_campaign(unittest.TestCase):
    """
    Basic testing for the campaign class.

    TODO:
        - complete all the functions
        - remove pass after completion of functions
    """

    def setUp(self):
        pass

    def test_get_people(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def test_get_name(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def test_add_people(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def test_remove_people(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def tearDown(self) -> None:
        (self)


class test_email(unittest.TestCase):
    """
    Basic Testing for the email class.

    TODO:
        - complete all the functions
        - remove pass after completion of functions
    """

    def setUp(self):
        pass

    def test_get_email_to(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def test_get_email_from(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def test_get_time_to_send(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def test_get_subject(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def test_get_template(self):
        """
        Basic testing to get the list of people in the campaign.
        """
        pass

    def tearDown(self) -> None:
        (self)


if __name__ == "__main__":
    unittest.main()
