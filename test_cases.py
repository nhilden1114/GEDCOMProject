from tables import user_story_1, user_story_2
from tables import user_story_3, user_story_4
from tables import user_story_5, user_story_6
from tables import user_story_18
from tables import user_story_21_a, user_story_21_b
from tables import Person

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

    def test_us2(self):
        indi = dict()
        #make person 1
        person = Person()
        person.idtag = 1
        indi[person.idtag] = person
        person.birth = datetime.datetime(1980, 5, 5)
        #make person 2
        person = Person()
        person.idtag = 2
        indi[person.idtag] = person
        person.birth = datetime.datetime(1985, 6, 26)

        self.assertEqual(user_story_2(indi, datetime.datetime(1990, 8, 16), 1, 2), True)
        self.assertEqual(user_story_2(indi, datetime.datetime(2010, 9, 23), 1, 2), True)
        self.assertEqual(user_story_2(indi, datetime.datetime(1980, 1, 5), 1, 2), False)
        self.assertEqual(user_story_2(indi, datetime.datetime(1983, 7, 13), 1, 2), False)
        self.assertEqual(user_story_2(indi, datetime.datetime(1985, 12, 30), 1, 2), True)

    def test_us3(self):
        self.assertTrue(user_story_3(datetime.datetime(1900, 2, 11), datetime.datetime(2000, 2, 11)), True)
        self.assertFalse(user_story_3(datetime.datetime(2000, 2, 11), datetime.datetime(1900, 2, 11)), False)
        self.assertFalse(user_story_3(datetime.datetime(3000, 2, 11), datetime.datetime(2000, 2, 11)), False)
        self.assertTrue(user_story_3(datetime.datetime(1999, 2, 11), datetime.datetime(1999, 2, 11)), True)
        self.assertFalse(user_story_3(datetime.datetime(1998, 2, 11), datetime.datetime(3000, 2, 12)), False)

    def test_us3(self):
        self.assertTrue(user_story_4(datetime.datetime(1900, 2, 11), datetime.datetime(2000, 2, 11)), True)
        self.assertFalse(user_story_4(datetime.datetime(2000, 2, 11), datetime.datetime(1900, 2, 11)), False)
        self.assertFalse(user_story_4(datetime.datetime(3000, 2, 11), datetime.datetime(2000, 2, 11)), False)
        self.assertTrue(user_story_4(datetime.datetime(1999, 2, 11), datetime.datetime(1999, 2, 11)), True)
        self.assertFalse(user_story_4(datetime.datetime(1998, 2, 11), datetime.datetime(3000, 2, 12)), False)

    def test_us6(self):
        self.assertTrue(user_story_6(datetime.datetime(1850, 3, 12), datetime.datetime(1950, 4, 17)), True)
        self.assertTrue(user_story_6(datetime.datetime(1950, 2, 14), datetime.datetime(2000, 6, 11)), True)
        self.assertFalse(user_story_6(datetime.datetime(2018, 5, 19), datetime.datetime(1918, 9, 25)), False)
        self.assertFalse(user_story_6(datetime.datetime(2017, 7, 20), datetime.datetime(1917, 7, 28)), False)
        self.assertFalse(user_story_6(datetime.datetime(2016, 8, 22), datetime.datetime(1926, 9, 10)), False)
    
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

    def test_us5(self):
        self.assertTrue(user_story_5(datetime.datetime(1850, 3, 12), datetime.datetime(1950, 4, 17)), True)
        self.assertTrue(user_story_5(datetime.datetime(1950, 2, 14), datetime.datetime(2000, 6, 11)), True)
        self.assertFalse(user_story_5(datetime.datetime(2018, 5, 19), datetime.datetime(1918, 9, 25)), False)
        self.assertFalse(user_story_5(datetime.datetime(2017, 7, 20), datetime.datetime(1917, 7, 28)), False)
        self.assertFalse(user_story_5(datetime.datetime(2016, 8, 22), datetime.datetime(1926, 9, 10)), False)
        
    def test_us21_a(self):
        indi = dict()
        i = 0
        while(i<1):
            person = Person()
            person.idtag = i
            indi[person.idtag] = person
            person.gender = 'M' #testing for a male husband
            i+=1
        self.assertEqual(user_story_21_a(indi, 0), True)
        j = 0
        while(j<1):
            person = Person()
            person.idtag = j
            indi[person.idtag] = person
            person.gender = 'F' #testing for a female husband
            j+=1
        self.assertEqual(user_story_21_a(indi, 0), False)
        k = 0
        while(k<1):
            person = Person()
            person.idtag = k
            indi[person.idtag] = person
            person.gender = 'hfjshdjshds' #testing for an incorrect husband
            k+=1
        self.assertEqual(user_story_21_a(indi, 0), False)
        
    def test_us21_b(self):
        indi = dict()
        i = 0
        while(i<1):
            person = Person()
            person.idtag = i
            indi[person.idtag] = person
            person.gender = 'F' #testing for a female wife
            i+=1
        self.assertEqual(user_story_21_b(indi, 0), True)
        j = 0
        while(j<1):
            person = Person()
            person.idtag = j
            indi[person.idtag] = person
            person.gender = 'M' #testing for a male wife
            j+=1
        self.assertEqual(user_story_21_b(indi, 0), False)
        k = 0
        while(k<1):
            person = Person()
            person.idtag = k
            indi[person.idtag] = person
            person.gender = 'hfjshdjshds' #testing for an incorrect wife
            k+=1
        self.assertEqual(user_story_21_b(indi, 0), False)
        


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
