import unittest

from Formated_name import get_formatted_name, get_formatted_name_3_names


class NamesTestCase(unittest.TestCase):
    """Tests for 'get_formatted_name.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name_3_names("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Mozart Amadeus")


unittest.main()
unittest.main()
