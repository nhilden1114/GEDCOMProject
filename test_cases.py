from tables import user_story_1, user_story_2
from tables import user_story_3, user_story_4
from tables import user_story_5, user_story_6
from tables import user_story_18
from tables import user_story_21_a, user_story_21_b
from tables import Person
from tables import createTables
#test comment
import unittest
import datetime


class Test(unittest.TestCase):

    def test_us1(self):
        '''
        Dates should not be after the current one
        '''
        self.assertEqual(user_story_1(datetime.datetime(2019, 3, 11)), False)
        self.assertEqual(user_story_1(datetime.datetime(2100, 11, 20)), False)
        self.assertEqual(user_story_1(datetime.datetime(2020, 1, 22)), False)
        self.assertEqual(user_story_1(datetime.datetime(2018, 9, 7)), True)
        self.assertEqual(user_story_1(datetime.datetime(2010, 8, 19)), True)
        self.assertEqual(user_story_1(datetime.datetime(1990, 3, 30)), True)

    def test_us2(self):
        '''
        Birth should occur before marriage
        '''

        file = open('NicoleFamily.ged', 'r')
        indi, fam = createTables(file)
        file.close()

        self.assertEqual(user_story_2(indi, datetime.datetime(1950, 8, 16), "@I02@", "@I03@"), False)
        self.assertEqual(user_story_2(indi, datetime.datetime(1990, 4, 11), "@I02@", "@I03@"), True)
        self.assertEqual(user_story_2(indi, datetime.datetime(1950, 3, 23), "@I04@", "@I05@"), True)
        self.assertEqual(user_story_2(indi, datetime.datetime(1990, 9, 14), "@I04@", "@I05@"), True)
        self.assertEqual(user_story_2(indi, datetime.datetime(1930, 1, 1), "@I04@", "@I05@"), False)

    def test_us3(self):
        '''
        A person's birthday must be before death date
        '''
        
        self.assertEqual(user_story_3(datetime.datetime.strptime('1900-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date()), True)
        self.assertEqual(user_story_3(datetime.datetime.strptime('2000-2-11','%Y-%m-%d').date(),datetime.datetime.strptime('1900-2-11','%Y-%m-%d').date()), False)
        self.assertEqual(user_story_3(datetime.datetime.strptime('3000-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date()), False)
        self.assertEqual(user_story_3(datetime.datetime.strptime('1999-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('1999-11-2','%Y-%m-%d').date()), True)
        self.assertEqual(user_story_3(datetime.datetime.strptime('1998-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('3000-11-2','%Y-%m-%d').date()), False)

    def test_us4(self):
        '''
        Divorce date should not be before marriage date
        '''
        
        self.assertEqual(user_story_4(datetime.datetime.strptime('1900-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date()), True)
        self.assertEqual(user_story_4(datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('1900-11-2','%Y-%m-%d').date()), False)
        self.assertEqual(user_story_4(datetime.datetime.strptime('3000-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date()), False)
        self.assertEqual(user_story_4(datetime.datetime.strptime('1999-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('1999-11-2','%Y-%m-%d').date()), True)
        self.assertEqual(user_story_4(datetime.datetime.strptime('1998-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('1997-11-2','%Y-%m-%d').date()), False)

##    def test_us6(self):
##        self.assertTrue(user_story_6(datetime.datetime(1850, 3, 12), datetime.datetime(1950, 4, 17)), True)
##        self.assertTrue(user_story_6(datetime.datetime(1950, 2, 14), datetime.datetime(2000, 6, 11)), True)
##        self.assertFalse(user_story_6(datetime.datetime(2018, 5, 19), datetime.datetime(1918, 9, 25)), False)
##        self.assertFalse(user_story_6(datetime.datetime(2017, 7, 20), datetime.datetime(1917, 7, 28)), False)
##        self.assertFalse(user_story_6(datetime.datetime(2016, 8, 22), datetime.datetime(1926, 9, 10)), False)
##    
##    def test_us18(self):
##        indi = dict()
##        i = 0
##        while(i<2):
##            person = Person()
##            person.idtag = i
##            indi[person.idtag] = person
##            person.famc = 2
##            i+=1
##        while(i<4):
##            person = Person()
##            person.idtag = i
##            indi[person.idtag] = person
##            person.famc = 1
##            i+=1
##        self.assertEqual(user_story_18(indi, 0, 2), True)
##        self.assertEqual(user_story_18(indi, 0, 1), False)
##        self.assertEqual(user_story_18(indi, 1, 2), True)
##        self.assertEqual(user_story_18(indi, 2, 3), False)
##        self.assertEqual(user_story_18(indi, 0, 3), True)
##
##    def test_us5(self):
##        self.assertTrue(user_story_5(datetime.datetime(1850, 3, 12), datetime.datetime(1950, 4, 17)), True)
##        self.assertTrue(user_story_5(datetime.datetime(1950, 2, 14), datetime.datetime(2000, 6, 11)), True)
##        self.assertFalse(user_story_5(datetime.datetime(2018, 5, 19), datetime.datetime(1918, 9, 25)), False)
##        self.assertFalse(user_story_5(datetime.datetime(2017, 7, 20), datetime.datetime(1917, 7, 28)), False)
##        self.assertFalse(user_story_5(datetime.datetime(2016, 8, 22), datetime.datetime(1926, 9, 10)), False)
##        
##    def test_us21_a(self):
##        indi = dict()
##        i = 0
##        while(i<1):
##            person = Person()
##            person.idtag = i
##            indi[person.idtag] = person
##            person.gender = 'M' #testing for a male husband
##            i+=1
##        self.assertEqual(user_story_21_a(indi, 0), True)
##        j = 0
##        while(j<1):
##            person = Person()
##            person.idtag = j
##            indi[person.idtag] = person
##            person.gender = 'F' #testing for a female husband
##            j+=1
##        self.assertEqual(user_story_21_a(indi, 0), False)
##        k = 0
##        while(k<1):
##            person = Person()
##            person.idtag = k
##            indi[person.idtag] = person
##            person.gender = 'hfjshdjshds' #testing for an incorrect husband
##            k+=1
##        self.assertEqual(user_story_21_a(indi, 0), False)
##        
##    def test_us21_b(self):
##        indi = dict()
##        i = 0
##        while(i<1):
##            person = Person()
##            person.idtag = i
##            indi[person.idtag] = person
##            person.gender = 'F' #testing for a female wife
##            i+=1
##        self.assertEqual(user_story_21_b(indi, 0), True)
##        j = 0
##        while(j<1):
##            person = Person()
##            person.idtag = j
##            indi[person.idtag] = person
##            person.gender = 'M' #testing for a male wife
##            j+=1
##        self.assertEqual(user_story_21_b(indi, 0), False)
##        k = 0
##        while(k<1):
##            person = Person()
##            person.idtag = k
##            indi[person.idtag] = person
##            person.gender = 'hfjshdjshds' #testing for an incorrect wife
##            k+=1
##        self.assertEqual(user_story_21_b(indi, 0), False)
##        


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
