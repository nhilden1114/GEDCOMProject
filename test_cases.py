from tables import user_story_1

import unittest

class Test(unittest.TestCase):

    def test_us1(self):
        self.assertEqual(user_story_1("11 MAR 2019"), False)
        self.assertEqual(user_story_1("10 OCT 2018"), False)
        self.assertEqual(user_story_1("22 JAN 2020"), False)
        self.assertEqual(user_story_1("07 SEP 2018"), True)
        self.assertEqual(user_story_1("19 AUG 2010"), True)
        self.assertEqual(user_story_1("30 MAR 1990"), True)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
