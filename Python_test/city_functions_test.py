import unittest
from city_functions import get_city_names

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do city and country names like 'Santiago, Chile' work?"""
        formatted_name = get_city_names('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

unittest.main()
