from tables import user_story_1

import unittest
import datetime

class Test(unittest.TestCase):

    def test_us1(self):
        self.assertEqual(user_story_1(datetime.datetime(2019, 3, 11)), False)
        self.assertEqual(user_story_1(datetime.datetime(2100, 11, 20)), False)
        self.assertEqual(user_story_1(datetime.datetime(2020, 1, 22)), False)
        self.assertEqual(user_story_1(datetime.datetime(2018, 9, 7)), True)
        self.assertEqual(user_story_1(datetime.datetime(2010, 8, 19)), True)
        self.assertEqual(user_story_1(datetime.datetime(1990, 3, 30)), True)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
