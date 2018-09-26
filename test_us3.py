"""

@author: Michayla Ben-Ezra -- September 25, 2018
The purpose of this test script is to test to see that the birth date for an individual is before their death date.

I pledge my honor that I have abided by the Stevens Honor System.
"""

from tables import user_story_3
import unittest
import datetime


class TestUserStory3(unittest.TestCase):

    def test_us3(self):
        self.assertTrue(user_story_3(datetime.datetime(1900, 2, 11), datetime.datetime(2000, 2, 11)), True)
        self.assertFalse(user_story_3(datetime.datetime(2000, 2, 11), datetime.datetime(1900, 2, 11)), False)
        self.assertFalse(user_story_3(datetime.datetime(3000, 2, 11), datetime.datetime(2000, 2, 11)), False)
        self.assertTrue(user_story_3(datetime.datetime(1999, 2, 11), datetime.datetime(1999, 2, 11)), True)
        self.assertFalse(user_story_3(datetime.datetime(1998, 2, 11), datetime.datetime(3000, 2, 12)), False)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()