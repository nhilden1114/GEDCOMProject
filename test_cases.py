from tables import user_story_1, user_story_2
from tables import user_story_3, user_story_4
from tables import user_story_5, user_story_6
from tables import user_story_7
from tables import user_story_18
from tables import user_story_21_a, user_story_21_b
from tables import user_story_22, user_story_29
from tables import create_tables
import unittest
import datetime


class Test(unittest.TestCase):

    def test_us1(self):
        """
        Dates should not be after the current one
        """
        self.assertEqual(user_story_1(datetime.datetime(2019, 3, 11)), False)
        self.assertEqual(user_story_1(datetime.datetime(2100, 11, 20)), False)
        self.assertEqual(user_story_1(datetime.datetime(2020, 1, 22)), False)
        self.assertEqual(user_story_1(datetime.datetime(2018, 9, 7)), True)
        self.assertEqual(user_story_1(datetime.datetime(2010, 8, 19)), True)
        self.assertEqual(user_story_1(datetime.datetime(1990, 3, 30)), True)

    def test_us2(self):
        """
        Birth should occur before marriage
        """

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_2(indi, datetime.datetime(1950, 8, 16), "@I02@", "@I03@"), False)
        self.assertEqual(user_story_2(indi, datetime.datetime(1990, 4, 11), "@I02@", "@I03@"), True)
        self.assertEqual(user_story_2(indi, datetime.datetime(1950, 3, 23), "@I04@", "@I05@"), True)
        self.assertEqual(user_story_2(indi, datetime.datetime(1990, 9, 14), "@I04@", "@I05@"), True)
        self.assertEqual(user_story_2(indi, datetime.datetime(1930, 1, 1), "@I04@", "@I05@"), False)

    def test_us3(self):
        """
        A person's birthday must be before death date
        """
        
        self.assertEqual(user_story_3(datetime.datetime.strptime('1900-11-2', '%Y-%m-%d').date(), datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date(), "Nicole"), True)
        self.assertEqual(user_story_3(datetime.datetime.strptime('2000-2-11', '%Y-%m-%d').date(), datetime.datetime.strptime('1900-2-11','%Y-%m-%d').date(), "Caroline"), False)
        self.assertEqual(user_story_3(datetime.datetime.strptime('3000-11-2', '%Y-%m-%d').date(), datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date(), "Michayla"), False)
        self.assertEqual(user_story_3(datetime.datetime.strptime('1999-11-2', '%Y-%m-%d').date(), datetime.datetime.strptime('1999-11-2','%Y-%m-%d').date(), "Elena"), True)
        self.assertEqual(user_story_3(datetime.datetime.strptime('1998-11-2', '%Y-%m-%d').date(), datetime.datetime.strptime('3000-11-2','%Y-%m-%d').date(), "David"), False)

    def test_us4(self):
        """
        Divorce date should not be before marriage date
        """
        
        self.assertEqual(user_story_4(datetime.datetime.strptime('1900-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date(), "Kevin", "Debbie"), True)
        self.assertEqual(user_story_4(datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('1900-11-2','%Y-%m-%d').date(), "Robert", "Judy"), False)
        self.assertEqual(user_story_4("NA",datetime.datetime.strptime('2000-11-2','%Y-%m-%d').date(), "Noel", "Carol"), False)
        self.assertEqual(user_story_4(datetime.datetime.strptime('1999-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('1999-11-2','%Y-%m-%d').date(), "John", "Jane"), True)
        self.assertEqual(user_story_4(datetime.datetime.strptime('1998-11-2','%Y-%m-%d').date(),datetime.datetime.strptime('1997-11-2','%Y-%m-%d').date(), "Kevin", "Debbie"), False)

    def test_us5(self):
        """
        A person cannot get married after their death
        """

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_5(datetime.datetime(1980, 8, 16), "@I08@", "@I09@", indi), False)
        self.assertEqual(user_story_5(datetime.datetime(1955, 10, 3), "@I08@", "@I09@", indi), True)
        self.assertEqual(user_story_5(datetime.datetime(1965, 2, 27), "@I08@", "@I09@", indi), True)
        self.assertEqual(user_story_5(datetime.datetime(2100, 7, 20), "@I01@", "@I03@", indi), False)
        self.assertEqual(user_story_5(datetime.datetime(2010, 7, 20), "@I01@", "@I03@", indi), True)

    def test_us6(self):
        """
        A person cannot get divorced after death
        """

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_6(datetime.datetime(1980, 8, 16), "@I08@", "@I09@", indi), False)
        self.assertEqual(user_story_6(datetime.datetime(1955, 10, 3), "@I08@", "@I09@", indi), True)
        self.assertEqual(user_story_6(datetime.datetime(1965, 2, 27), "@I08@", "@I09@", indi), True)
        self.assertEqual(user_story_6(datetime.datetime(2000, 7, 20), "@I01@", "@I03@", indi), True)
        self.assertEqual(user_story_6(datetime.datetime(2019, 7, 20), "@I01@", "@I04@", indi), False)

    def test_us7(self):
        """
        A person cannot be more than 150 years old
        """

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_7(datetime.datetime(1900, 8, 16), datetime.datetime(1980, 8, 16), "Nicole"), True)
        self.assertEqual(user_story_7(datetime.datetime(1800, 8, 16), datetime.datetime(1980, 8, 16), "David"), False)
        self.assertEqual(user_story_7(datetime.datetime(1800, 8, 16), datetime.datetime(1980, 8, 16), "David"), False)
        self.assertEqual(user_story_7(datetime.datetime(1800, 8, 16), datetime.datetime(1980, 8, 16), "David"), False)
        self.assertEqual(user_story_7(datetime.datetime(1800, 8, 16), datetime.datetime(1980, 8, 16), "David"), False)
        self.assertEqual(user_story_7(datetime.datetime(1800, 8, 16), datetime.datetime(1980, 8, 16), "David"), False)

    def test_us18(self):
        """
        Siblings should not marry
        """

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_18(indi, "@I01@", "@I06@"), False)
        self.assertEqual(user_story_18(indi, "@I03@", "@I07@"), False)
        self.assertEqual(user_story_18(indi, "@I02@", "@I12@"), False)
        self.assertEqual(user_story_18(indi, "@I02@", "@I03@"), True)
        self.assertEqual(user_story_18(indi, "@I08@", "@I09@"), True)


    def test_us21_a(self):
        """
        Correct gender for husband
        """

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()
        
        self.assertEqual(user_story_21_a(indi, "@I02@", "John"), True)
        self.assertEqual(user_story_21_a(indi, "@I01@", "Jane"), False)
        self.assertEqual(user_story_21_a(indi, "@I04@", "Simon"), True)
        self.assertEqual(user_story_21_a(indi, "@I03@", "Caroline"), False)
        self.assertEqual(user_story_21_a(indi, "@I07@", "David"), False)
       
    def test_us21_b(self):
        """
        Correct gender for wife
        """

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()
        
        self.assertEqual(user_story_21_b(indi, "@I02@", "David"), False)
        self.assertEqual(user_story_21_b(indi, "@I01@", "Nicole"), True)
        self.assertEqual(user_story_21_b(indi, "@I04@", "Kevin"), False)
        self.assertEqual(user_story_21_b(indi, "@I03@", "Ann"), True)
        self.assertEqual(user_story_21_b(indi, "@I07@", "Michayla"), True)

    def test_us22(self):
        """
        No duplicate id tags in file
        """

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_22(indi))

        file = open('us_22.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_22(indi))

        file = open('us_15.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_22(indi))

    def test_us29(self):
        """
        List deceased
        """
        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_29(indi), ['@I01@', '@I08@'])
        self.assertNotEqual(user_story_29(indi), [])
        self.assertNotEqual(user_story_29(indi), ['@F1@'])
        self.assertNotEqual(user_story_29(indi), ['@T07@'])
        self.assertNotEqual(user_story_29(indi), ['@I01@', '@I08@', '@F1@'])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
