from tables import determine_age
from tables import user_story_1, user_story_2
from tables import user_story_3, user_story_4
from tables import user_story_5, user_story_6
from tables import user_story_7, user_story_10
from tables import user_story_11, user_story_13
from tables import user_story_18, user_story_15
from tables import user_story_21_a, user_story_21_b
from tables import user_story_22, user_story_23
from tables import user_story_25
from tables import user_story_29, user_story_30
from tables import user_story_34, user_story_35
from tables import user_story_36, user_story_38
from tables import create_tables, create_indi, create_fam
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

        file = open('user_story_geds/us3.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_3(indi, "@US3_I1@"), False)
        self.assertEqual(user_story_3(indi, "@US3_I2@"), True)
        self.assertEqual(user_story_3(indi, "@US3_I3@"), True)
        self.assertEqual(user_story_3(indi, "@US3_I4@"), False)
        self.assertEqual(user_story_3(indi, "@US3_I5@"), False)

    def test_us4(self):
        """
        Divorce date should not be before marriage date
        """

        file = open('user_story_geds/us4.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_4(fam, "@US4_F1@"), False)
        self.assertEqual(user_story_4(fam, "@US4_F2@"), True)
        self.assertEqual(user_story_4(fam, "@US4_F3@"), True)
        self.assertEqual(user_story_4(fam, "@US4_F4@"), False)
        self.assertEqual(user_story_4(fam, "@US4_F5@"), True)

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

        self.assertEqual(user_story_7(datetime.datetime(1900, 8, 16), datetime.datetime(1980, 8, 16), "Nicole"), True)
        self.assertEqual(user_story_7(datetime.datetime(1800, 3, 10), datetime.datetime(1988, 9, 12), "David"), False)
        self.assertEqual(user_story_7(datetime.datetime(1852, 1, 2), datetime.datetime.today(), "Caroline"), False)
        self.assertEqual(user_story_7(datetime.datetime(1990, 9, 22), datetime.datetime.today(), "Michayla"), True)
        self.assertEqual(user_story_7(datetime.datetime(1492, 7, 9), datetime.datetime(2000, 8, 16), "Elena"), False)

    def test_us10(self):
        '''
        Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
        '''

        file = open('user_story_geds/us10.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_10(indi, "@US10_F01@", fam), True)
        self.assertEqual(user_story_10(indi, "@US10_F02@", fam), False)
        self.assertEqual(user_story_10(indi, "@US10_F03@", fam), False)
        self.assertEqual(user_story_10(indi, "@US10_F04@", fam), True)
        self.assertEqual(user_story_10(indi, "@US10_F05@", fam), True)

    def test_us11(self):
        '''
        Marriage should not occur during marriage to another spouse
        '''

        file = open('user_story_geds/us11.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_11(indi, fam, "@US11_I01@", "@US11_I02@"), False)
        self.assertEqual(user_story_11(indi, fam, "@US11_I02@", "@US11_I03@"), False)
        self.assertEqual(user_story_11(indi, fam, "@US11_I03@", "@US11_I04@"), True)
        self.assertEqual(user_story_11(indi, fam, "@US11_I04@", "@US11_I07@"), True)
        self.assertEqual(user_story_11(indi, fam, "@US11_I05@", "@US11_I07@"), False)

    def test_us13(self):
        '''
        Birth dates of siblings should be more than 8 months apart or less than 2 days apart
        '''
        
        #file = open('user_story_geds/us13.ged', 'r')
        #indi, fam = create_tables(file)
        #file.close()
        
        #print("...................................................... " + str(user_story_13(indi, fam)))
        
        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_13(indi, fam), True)

        file = open('user_story_geds/us11.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_13(indi, fam), True)

        file = open('user_story_geds/us22.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_13(indi, fam), True)

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_13(indi, fam), True)

        file = open('user_story_geds/us07.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertEqual(user_story_13(indi, fam), True)


    def test_us15(self):
        '''
        There should be fewer than 15 siblings in a family
        '''

        # file = open('user_story_geds/us15.ged', 'r')
        # indi, fam = create_tables(file)
        # file.close()

        # families = []
        # family_tags = []
        # for family in fam:
        #   family_tags.append(family)
        #  families.append(fam[family].chil)

        # self.assertTrue(user_story_15(families[0], family_tags[0]))
        # self.assertFalse(user_story_15(families[1], family_tags[1]))
        # self.assertTrue(user_story_15(families[2], family_tags[2]))
        # self.assertTrue(user_story_15(families[3], family_tags[3]))
        self.assertTrue(user_story_15(["Nicole", "Caroline"], "Test fam of 2"))
        self.assertTrue(user_story_15(["Nicole", "Caroline", "Elena", "Michayla"], "Test fam of 4"))
        self.assertTrue(user_story_15(["Nicole", "Caroline", "Elena", "Michayla", "Ann", "David"], "Test fam of 6"))
        self.assertTrue(user_story_15(["Nicole", "Caroline", "Elena"], "Test fam of 3"))
        self.assertFalse(user_story_15(
            ["Nicole", "Caroline", "Elena", "Michayla", "Ann", "David", "John", "Mary", "Vince", "Bob", "Kiki", "AJ",
             "JJ", "AA", "BB", "CC"], "Test_fam_of_16"))

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

        file = open('user_story_geds/us22.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_22(indi, "TAG1"))
        self.assertTrue(user_story_22(indi, "TAG2"))
        self.assertTrue(user_story_22(indi, "TAG3"))
        self.assertFalse(user_story_22(indi, "@US22_I1@"))
        self.assertFalse(user_story_22(indi, "@US22_I2@"))

    def test_us23(self):
        """
        No more than one individual with the same name and birth date should appear in a GEDCOM file
        """

        file = open('user_story_geds/us23.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertFalse(user_story_23(indi))

        file = open('user_story_geds/us07.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_23(indi))

        file = open('user_story_geds/us11.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_23(indi))

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_23(indi))

        file = open('user_story_geds/us01.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_23(indi))
     
    def test_us25(self):
        """
        No more than one child with the same name and birth date should appear in a family
        """
        
        file = open('user_story_geds/us23.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_25(indi, fam))

        file = open('user_story_geds/us07.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_25(indi, fam))

        file = open('user_story_geds/us11.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_25(indi, fam))

        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_25(indi, fam))

        file = open('user_story_geds/us34.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        self.assertTrue(user_story_25(indi, fam))
     

    def test_us27(self):
        '''
        Test that individuals ages are calculated
        '''
        self.assertEqual(determine_age(datetime.date(2000, 1, 1), datetime.date.today()), 18) 
        self.assertEqual(determine_age(datetime.date(2000, 11, 30), datetime.date.today()), 17) 
        self.assertEqual(determine_age(datetime.date(1990, 7, 22), datetime.date.today()), 28) 
        self.assertEqual(determine_age(datetime.date(1990, 12, 25), datetime.date.today()), 27) 
        self.assertEqual(determine_age(datetime.date(2020, 1, 1), datetime.date.today()), -2) 
        self.assertEqual(determine_age(datetime.date(1818, 1, 1), datetime.date.today()), 200) 

    def test_us29(self):
        """
        List deceased
        """
        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        result = user_story_29(indi)

        self.assertIn("@I01@", result)
        self.assertIn("@I08@", result)
        self.assertNotIn("@I10@", result)
        self.assertNotIn("@I09@", result)
        self.assertNotIn("@I05@", result)

    def test_us30(self):
        '''
        List all living married people in a GEDCOM file
        '''
        file = open('NicoleFamily.ged', 'r')
        indi, fam = create_tables(file)
        file.close()

        result = user_story_30(indi, fam)

        self.assertIn("@I04@", result)
        self.assertIn("@I05@", result)
        self.assertIn("@I09@", result)
        self.assertIn("@I10@", result)
        self.assertNotIn("@I08@", result)

    def test_us34(self):
        '''
        List all couples who were married when the older spouse was more than twice as old as the younger spouse
        '''
        file = open('user_story_geds/us34.ged')
        indi, fam = create_tables(file)
        file.close()

        result = user_story_34(indi, fam)

        self.assertNotIn("@US34_I03@", result)
        self.assertNotIn("@US34_I04@", result)
        self.assertNotIn("@US34_I07@", result)
        self.assertNotIn("@US34_I10@", result)
        self.assertIn("@US34_I01@", result)
        self.assertIn("@US34_I02@", result)
        self.assertIn("@US34_I05@", result)
        self.assertIn("@US34_I06@", result)
        
    def test_us35(self):
        """
        List all people born in the past 30 days
        """
        file = open('user_story_geds/us35.ged')
        indi, fam = create_tables(file)
        file.close()

        result = user_story_35(indi)
        self.assertIn("@US35_I1@", result)
        self.assertIn("@US35_I4@", result)
        self.assertNotIn("@US35_I3@", result)
        self.assertNotIn("@US35_I5@", result)
        self.assertNotIn("@US35_I20@", result)

    def test_us36(self):
        """
        List all people born in the past 30 days
        """
        file = open('user_story_geds/us36.ged')
        indi, fam = create_tables(file)
        file.close()

        result = user_story_36(indi)
        self.assertIn("@US36_I2@", result)
        self.assertIn("@US36_I6@", result)
        self.assertNotIn("@US36_I3", result)
        self.assertNotIn("@US36_I5@", result)
        self.assertNotIn("@US36_I20@", result)

    def test_us38(self):
        """
        List all living people with birthdays in the next 30 days
        """
        file = open('user_story_geds/us38.ged')
        indi, fam = create_tables(file)
        file.close()

        result = user_story_38(indi)
        self.assertIn("@US38_I1@", result)
        self.assertIn("@US38_I3@", result)
        self.assertIn("@US38_I4@", result)
        self.assertNotIn("@US38_I2@", result)
        self.assertNotIn("@US38_I5@", result)



if __name__ == '__main__':
    print('Running unit tests')
    file = open('user_story_geds/bigged.ged', 'r')
    indi, fam = create_tables(file)
    create_indi(indi)
    create_fam(fam)
    file.close()

    unittest.main(exit = False, verbosity = 2)


