from tables import user_story_1, user_story_18
from tables import Person

import unittest
import datetime

class Test(unittest.TestCase):

    #def test_us1(self):
     #   self.assertEqual(user_story_1(datetime.datetime(2019, 3, 11)), False)
      #  self.assertEqual(user_story_1(datetime.datetime(2100, 11, 20)), False)
       # self.assertEqual(user_story_1(datetime.datetime(2020, 1, 22)), False)
        #self.assertEqual(user_story_1(datetime.datetime(2018, 9, 7)), True)
        #self.assertEqual(user_story_1(datetime.datetime(2010, 8, 19)), True)
        #self.assertEqual(user_story_1(datetime.datetime(1990, 3, 30)), True)
    
    def test_us18(self):
        indi = dict()
        i = 0
        while(i<2):
            person = Person()
            person.idtag = i
            indi[person.idtag] = person
            person.famc = 2
            i+=1
        while(i<4):
            person = Person()
            person.idtag = i
            indi[person.idtag] = person
            person.famc = 1
            i+=1
        self.assertEqual(user_story_18(indi, 0, 2), True)
        self.assertEqual(user_story_18(indi, 0, 1), False)
        self.assertEqual(user_story_18(indi, 1, 2), True)
        self.assertEqual(user_story_18(indi, 2, 3), False)
        self.assertEqual(user_story_18(indi, 0, 3), True)

        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
