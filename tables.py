from prettytable import PrettyTable
import datetime
from datetime import date
from Project3 import validLine


def determine_age(dob, date):
    """
       Calculate the age of a person given two dates
       dob is the person's date of birth
       date is either the current date or the death date
    """
    age = date.year - dob.year - ((dob.month, dob.day) > (date.month, date.day))

    # age = abs((date – dob)).days / 365.25

    return age


def calc_difference(date1, date2):
    '''Calculates the difference between 2 dates'''
    return date2.year - date1.year - ((date1.month, date1.day) > (date2.month, date2.day))


def user_story_1(inputDate):
    '''
    Dates (birth, marriage, divorce, death) should not be after the current date
    inputDate can be a birthday, death date, date of marriage or divorce
    '''

    current = date.today()

    if calc_difference(inputDate, current) < 0:
        print("ERROR: US01: Date: " + inputDate.strftime('%Y-%m-%d') + " should not be after the current one")
        return False
    else:
        return True


def user_story_2(indi, marr_date, husbid, wifeid):
    '''
    Birth should occur before marriage of an individual
    indi is the table of all individuals in the GEDCOM file
    marr_date is the marriage date
    husbid is the id of the husband of this marriage
    wifeid is the id of the wife of this marriage
    '''

    wife_diff = calc_difference(indi[wifeid].birth, marr_date)
    husb_diff = calc_difference(indi[husbid].birth, marr_date)

    if wife_diff < 0:
        print("ERROR: US02: Marriage date of " + marr_date.strftime('%Y-%m-%d') + " cannot be before Birth date of " +
              indi[wifeid].name + " which is " + indi[wifeid].birth.strftime('%Y-%m-%d'))
        return False
    if husb_diff < 0:
        print("ERROR: US02: Marriage date of " + marr_date.strftime('%Y-%m-%d') + " cannot be before Birth date of " +
              indi[husbid].name + " which is " + indi[husbid].birth.strftime('%Y-%m-%d'))
        return False
    else:
        return True


def user_story_3(birthday, death_day, name):  # a person's birthday must be before their death date
    # I added the back because the tests got messed up, will fix!
    if birthday != "NA" and birthday < date.today():
        if death_day != "NA" and death_day <= date.today():
            if calc_difference(birthday, death_day) < 0:
                print("ERROR: US03: Death date of " + death_day.strftime(
                    '%Y-%m-%d') + " should not be before " + name + "'s birth date of " + birthday.strftime('%Y-%m-%d'))
                return False
            else:
                return True
        else:
            print("ERROR: US03: Death date of " + death_day.strftime('%Y-%m-%d') + " is not valid")
            return False
    else:
        print("ERROR: US03: Birth date of " + birthday.strftime('%Y-%m-%d') + " is not valid")
        return False


def user_story_4(marriage_date, divorce_date, husbname, wifename):  # Divorce date should not be before marriage date

    if marriage_date != "NA" and marriage_date < date.today():
        difference = divorce_date.year - marriage_date.year - (
                (marriage_date.month, marriage_date.day) > (divorce_date.month, divorce_date.day))

        if difference < 0:
            print("ERROR: US04: Divorce date of " + divorce_date.strftime(
                '%Y-%m-%d') + " should not be before the marriage date of " + marriage_date.strftime(
                '%Y-%m-%d') + " for " + husbname + " and " + wifename)
            return False
        else:
            return True
    else:
        print(
            "ERROR: US04: Marriage date of " + marriage_date + " not valid " + " for " + husbname + " and " + wifename)
        return False


def user_story_5(marriage_date, husbid, wifeid, indi):  # A person cannot get married after their death date

    deaths = [[indi[husbid].death, indi[husbid].name], [indi[wifeid].death, indi[wifeid].name]]

    for death_date in deaths:
        dday = death_date[0]
        if dday != "NA":
            difference = dday.year - marriage_date.year - (
                    (marriage_date.month, marriage_date.day) > (dday.month, dday.day))
            if difference < 0:
                print("ERROR: US05: Marriage date of " + marriage_date.strftime(
                    '%Y-%m-%d') + " should not occur after death date for " + death_date[
                          1] + " which is " + dday.strftime('%Y-%m-%d'))
                return False
            else:
                return True
        return True


def user_story_6(divorce_date, husbid, wifeid, indi):  # A person cannot get a divorce after death

    deaths = [[indi[husbid].death, indi[husbid].name], [indi[wifeid].death, indi[wifeid].name]]

    for death_date in deaths:
        dday = death_date[0]
        if dday != "NA":
            difference = dday.year - divorce_date.year - (
                    (divorce_date.month, divorce_date.day) > (dday.month, dday.day))
            if difference < 0:
                print("ERROR: US06: Divorce date of " + divorce_date.strftime(
                    '%Y-%m-%d') + " should not occur after death date for " + death_date[
                          1] + " which is " + dday.strftime('%Y-%m-%d'))
                return False
            else:
                return True
        return True


def user_story_7(birth, comp_date, name):
    '''
    Death should be less than 150 years after birth for dead people,
    and current date should be less than 150 years after birth for all living people
    Comp date is either the current date or the death date
    '''

    # difference = comp_date.year - birth.year - ((birth.month, birth.day) > (comp_date.month, comp_date.day))
    if calc_difference(birth, comp_date) >= 150:
        print("ERROR: US07: " + name + " must be less than 150 years old")
        return False
    return True


"""def user_story_14(indi, fam, birth, idtag):
    siblings = indi[idtag].chil
    birthdays = []

    for i > 0 in siblings:
"""


def user_story_15(child_list, family_tag):  # There should be fewer than 15 siblings in a family
    if len(child_list) < 15:
        return True
    else:
        print("ERROR: US15: There should be fewer than 15 siblings in family " + family_tag)
        return False


def user_story_18(indi, husbid, wifeid):  # Siblings should NOT marry
    husb_fam = indi[husbid].famc
    wife_fam = indi[wifeid].famc

    if husb_fam != [] and wife_fam != []:
        if husb_fam == wife_fam:
            print("ERROR: US18: Incest occurring with " + str(indi[husbid].name) + " and " + str(indi[wifeid].name))
            return False
        else:
            return True
    return True


def user_story_21_a(indi, husbid, name):  # Correct gender role for husband
    husb_gender = indi[husbid].gender

    if husb_gender == "M":
        return True
    else:
        print("ERROR: US21: Incorrect gender " + husb_gender + " for husband " + name)
        return False


def user_story_21_b(indi, wifeid, name):  # Correct gender role for wife
    wife_gender = indi[wifeid].gender

    if wife_gender == "F":
        return True
    else:
        print("ERROR: US21: Incorrect gender " + wife_gender + " for wife " + name)
        return False


def user_story_22(indi):  # ensure only unique ids
    unique = list()

    for i in indi:
        unique.append(indi[i].idtag)
    if len(unique) == len(set(unique)):
        return True
    else:
        print("ERROR: US22: duplicate individual ids found in file")


def user_story_29_helper(indi, idtag):  # to only return the idtags of people who are deceased
    death_status = indi[idtag].death
    if death_status != 'NA':
        return idtag
    else:
        return None


def user_story_29(indi):  # return a list of the deceased
    deceased = []

    for i in indi:
        temp = user_story_29_helper(indi, i)
        if temp:
            deceased.append(temp)
    return deceased


class Person:

    def __init__(self):
        self.idtag = "NA"
        self.name = "NA"
        self.gender = "NA"
        self.birth = "NA"
        self.age = "NA"
        self.alive = True
        self.death = "NA"
        self.famc = list()
        self.fams = list()


class Family:

    def __init__(self):
        self.idtag = "NA"
        self.marr = "NA"
        self.div = "NA"
        self.husbid = "NA"
        self.husbnam = "NA"
        self.wifeid = "NA"
        self.wifename = "NA"
        self.chil = list()


def create_tables(file):
    indi = dict()  # indi[id] = instance of class Person
    fam = dict()  # fam[id] = instance of class Family

    arr = file.readlines()

    i = 0
    person = None
    family = None

    while i < len(arr):
        line = arr[i].strip()
        level, tag, args, tokens = validLine(line)

        i += 1

        if tag is not None:

            if tag == "INDI":
                person = Person()
                person.idtag = args
                indi[person.idtag] = person

            elif tag == "FAM":
                family = Family()
                family.idtag = args
                fam[family.idtag] = family

            elif tag == "NAME":
                person.name = args

            elif tag == "SEX":
                person.gender = args

            elif tag == "BIRT":

                # need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)

                if new_tag == "DATE":
                    new_date = datetime.datetime.strptime(new_args, "%d %b %Y").date()
                    if user_story_1(new_date):  # test that date is not in future
                        if user_story_7(new_date, datetime.datetime.today(), person.name):  # test <150 years old
                            x = 3
                            # person.birth = new_date
                            # person.age = determine_age(new_date, datetime.datetime.today())
                person.birth = new_date
                person.age = determine_age(new_date, datetime.datetime.today())

            elif tag == "DEAT":
                person.alive = False

                # need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)

                if new_tag == "DATE":
                    new_date = datetime.datetime.strptime(new_args, "%d %b %Y").date()
                    # print("testing deaths " + " death: " + new_args + " name: " + person.name + " birth: " + person.birth)
                    if user_story_1(new_date):  # test that date is not in the future
                        if user_story_3(person.birth, new_date, person.name):  # test that death is after birth
                            if user_story_7(person.birth, new_date, person.name):  # test <150 years old
                                x = 3
                                # person.death = new_date
                                # person.age = determine_age(person.birth, new_date)
                person.death = new_date
                person.age = determine_age(person.birth, new_date)


            elif tag == "FAMS":
                person.fams.append(args)

            elif tag == "FAMC":
                person.famc.append(args)

            elif tag == "MARR":

                # need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)

                if new_tag == "DATE":
                    new_date = datetime.datetime.strptime(new_args, "%d %b %Y").date()
                    if user_story_1(new_date):  # check date not in future
                        if user_story_2(indi, new_date, family.husbid, family.wifeid):  # check birth before marriage
                            if user_story_18(indi, family.husbid, family.wifeid):  # check not siblings
                                if user_story_5(new_date, family.husbid, family.wifeid,
                                                indi):  # check marr before death
                                    if user_story_21_a(indi, family.husbid, family.husbname) and user_story_21_b(indi,
                                                                                                                 family.wifeid,
                                                                                                                 family.wifename):  # check genders
                                        family.marr = new_date

            elif tag == "DIV":

                # need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)

                if new_tag == "DATE":
                    new_date = datetime.datetime.strptime(new_args, "%d %b %Y").date()
                    if user_story_1(new_date):  # test that date is not in future
                        if user_story_4(family.marr, new_date, family.husbname,
                                        family.wifename):  # check div after marr
                            if user_story_6(new_date, family.husbid, family.wifeid, indi):  # check no div after death
                                family.div = new_date

            elif tag == "HUSB":
                family.husbid = args
                family.husbname = indi[args].name

            elif tag == "WIFE":
                family.wifeid = args
                family.wifename = indi[args].name

            elif tag == "CHIL":
                if user_story_15(family.chil, family.idtag):
                    family.chil.append(args)

    return indi, fam


def create_indi(indi):
    table = PrettyTable()
    table.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

    for key in sorted(indi.keys()):
        idt = indi[key].idtag
        nam = indi[key].name
        gen = indi[key].gender
        bir = indi[key].birth
        dea = indi[key].death
        age = indi[key].age
        ali = indi[key].alive
        fc = indi[key].famc
        fs = indi[key].fams
        table.add_row([idt, nam, gen, bir, age, ali, dea, fc, fs])

    print(table)


def create_fam(fam):
    table = PrettyTable()
    table.field_names = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    for key in sorted(fam.keys()):
        idt = fam[key].idtag
        mar = fam[key].marr
        div = fam[key].div
        hus = fam[key].husbname
        hid = fam[key].husbid
        wif = fam[key].wifename
        wid = fam[key].wifeid
        chi = fam[key].chil
        table.add_row([idt, mar, div, hid, hus, wid, wif, chi])

    print(table)


def main():
    """ Need to put a descriptive docstring here"""
    try:
        # file = open('us_15.ged', 'r')
        file = open('NicoleFamily.ged', 'r')
        # file = open('user_story_geds/us15.ged', 'r')
    except:
        print("Cannot open file")

    indi_info, fam_info = create_tables(file)

    create_indi(indi_info)
    create_fam(fam_info)


if __name__ == '__main__':
    main()
