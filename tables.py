from prettytable import PrettyTable
import datetime
from datetime import date, timedelta
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
    '''
    Calculates the difference between 2 dates
    '''
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
    indi is the dict of all individuals in the GEDCOM file
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


def user_story_3(birthday, death_day, name):
    '''
    A person's birthday must be before their death date
    birthday is the birthday of the person
    death_day is the date of death of the person
    name is the person's name
    '''

    if birthday != "NA":  # and birthday < date.today():
        if death_day != "NA":  # and death_day <= date.today():
            if calc_difference(birthday, death_day) < 0:
                print("ERROR: US03: Death date of " + death_day.strftime(
                    '%Y-%m-%d') + " should not be before " + name + "'s birth date of " + birthday.strftime('%Y-%m-%d'))
                return False
            else:
                return True


##        else:
##            print("ERROR: US03: Death date of " + death_day.strftime('%Y-%m-%d') + " is not valid")
##            return False
##    else:
##        print("ERROR: US03: Birth date of " + birthday.strftime('%Y-%m-%d') + " is not valid")
##        return False


def user_story_4(marriage_date, divorce_date, husbname, wifename):
    '''
    Divorce date should not be before the marriage date
    marriage_date is the marriage date
    divorce_date is the date of divorce
    husbname is the name of the husband
    wifename is the name of the wife
    '''
    if divorce_date == "NA":
        return True

    if marriage_date != "NA":

        if calc_difference(marriage_date, divorce_date) < 0:
            print("ERROR: US04: Divorce date of " + divorce_date.strftime(
                '%Y-%m-%d') + " should not be before the marriage date of " + marriage_date.strftime(
                '%Y-%m-%d') + " for " + husbname + " and " + wifename)
            return False
        else:
            return True
    else:
        if marriage_date == "NA":
            print(
                "ERROR: US04: Marriage date of " + marriage_date + " not valid " + " for " + husbname + " and " + wifename)
            return False


def user_story_5(marriage_date, husbid, wifeid, indi):
    '''
    A person cannot get married after their death date
    marriage_date is the date of marriage
    husbid is the id of the husband
    wifeid is the id of the wife
    indi is the dictionary that contains all individuals in the file
    '''

    if marriage_date == "NA":
        return True

    deaths = [[indi[husbid].death, indi[husbid].name], [indi[wifeid].death, indi[wifeid].name]]

    for death_date in deaths:
        dday = death_date[0]
        if dday != "NA":
            if calc_difference(marriage_date, dday) < 0:
                print("ERROR: US05: Marriage date of " + marriage_date.strftime(
                    '%Y-%m-%d') + " should not occur after death date for " + death_date[
                          1] + " which is " + dday.strftime('%Y-%m-%d'))
                return False
            else:
                return True
        return True


def user_story_6(divorce_date, husbid, wifeid, indi):
    '''
    A person cannot get a divorce after death
    divorce_date is the date of divorce
    husbid is the id of the husband
    wifeid is the id of the wife
    indi is the dictionary that contains all individuals in the file
    '''

    if divorce_date == "NA":
        return True

    deaths = [[indi[husbid].death, indi[husbid].name], [indi[wifeid].death, indi[wifeid].name]]

    for death_date in deaths:
        dday = death_date[0]
        if dday != "NA":
            if calc_difference(divorce_date, dday) < 0:
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
    if birth == "NA":
        return True

    if comp_date == "NA":
        comp_date = date.today()

    if calc_difference(birth, comp_date) >= 150:
        print("ERROR: US07: " + name + " must be less than 150 years old")
        return False
    return True


def user_story_10(indi, family, fam):
    '''
    Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
    indi is the dict of individuals
    family is the current family tag
    fam is the dict of families
    '''

    if fam[family].marr == "NA":
        return True

    wife_diff = calc_difference(indi[fam[family].wifeid].birth, fam[family].marr)
    husb_diff = calc_difference(indi[fam[family].husbid].birth, fam[family].marr)

    if wife_diff < 14:
        print("ERROR: US10: Marriage date of " + fam[family].marr.strftime('%Y-%m-%d') + " cannot occur because " + fam[
            family].wifename + " is under 14 years of age")
        return False

    elif husb_diff < 14:
        print("ERROR: US10: Marriage date of " + fam[family].marr.strftime('%Y-%m-%d') + " cannot occur because " + fam[
            family].husbname + " is under 14 years of age")
        return False

    return True


def user_story_11(indi, fam, husbid, wifeid):
    '''
    Marriage should not occur during marriage to another spouse
    indi is the dict of all individuals in the GEDCOM file
    fam is the dict of all families in the GEDCOM file
    husbid is the husband's id
    wifeid is the wife's id
    '''
    if len(indi[husbid].fams) > 1:
        for family_h in indi[husbid].fams:
            this_wife = fam[family_h].wifeid
            if fam[family_h].div != "NA":# or indi[this_wife].death != "NA":
                continue
            elif fam[family_h].div == "NA":
                print("ERROR: US11: " + indi[husbid].name + " is not divorced yet from " + indi[this_wife].name)
                return False
            elif indi[this_wife].death == "NA":
                print("ERROR: US11: " + indi[husbid].name + "'s wife " + indi[
                    this_wife].name + " is still alive and married to him")
                return False
    if len(indi[wifeid].fams) > 1:
        for family_w in indi[wifeid].fams:
            this_husb = fam[family_w].husbid
            if fam[family_w].div != "NA":# or indi[this_husb].death != "NA":
                continue
            elif fam[family_w].div == "NA":
                print("ERROR: US11: " + indi[wifeid].name + " is not divorced yet from " + indi[this_husb].name)
                return False
            elif indi[this_husb].death == "NA":
                print("ERROR: US11: " + indi[wifeid].name + "'s husband " + indi[
                    this_husb].name + " is still alive and married to her")
                return False
    return True


def user_story_13(indi, fam):
    '''
    Birth dates of siblings should be more than 8 months apart or less than 2 days apart
    indi is the dict of all individuals in the GEDCOM file
    fam is the dict of all families in the GEDCOM file
    '''
    flag = True
    for family in fam:
        births = list()
        for child in fam[family].chil:
            if indi[child].birth != "NA":
                births.append(indi[child].birth)
        for i in range(len(births)):
            if i + 1 < len(births):
                if births[i] > births[i + 1]:
                    if (births[i] - births[i + 1]).days > 2 and (births[i] - births[i + 1]).days < 243:
                        flag = False
                        print("ERROR: US13: Birthdate of " + births[i].strftime(
                            '%Y-%m-%d') + " is too soon after birthday of sibling on " + births[i + 1].strftime(
                            '%Y-%m-%d'))
                elif (births[i + 1] - births[i]).days > 2 and (births[i + 1] - births[i]).days < 243:
                    flag = False
                    print("ERROR: US13: Birthdate of " + births[i + 1].strftime(
                        '%Y-%m-%d') + " is too soon after birthday of sibling on " + births[i].strftime('%Y-%m-%d'))
    return flag


def user_story_15(child_list, family_tag):
    '''
    There should be fewer than 15 siblings in a family
    child_list is the list of all children in a family
    family_tag is the current family from the fam table
    '''

    if len(child_list) < 15:
        return True
    else:
        print("ERROR: US15: There should be fewer than 15 siblings in family " + family_tag)
        return False


def user_story_18(indi, husbid, wifeid):
    '''
    Siblings should NOT marry
    indi is the dict of all individuals
    husbid is the id of the husband
    wifeid is the id of the wife
    '''
    husb_fam = indi[husbid].famc
    wife_fam = indi[wifeid].famc

    if husb_fam != [] and wife_fam != []:
        if husb_fam == wife_fam:
            print("ERROR: US18: Incest occurring with " + str(indi[husbid].name) + " and " + str(indi[wifeid].name))
            return False
        else:
            return True
    return True


def user_story_21_a(indi, husbid, name):
    '''
    Correct gender role for husband
    indi is the dict of all individuals
    husbid is the id of the husband
    name is the name of the husband
    '''

    husb_gender = indi[husbid].gender

    if husb_gender == "M":
        return True
    else:
        print("ERROR: US21: Incorrect gender " + husb_gender + " for husband " + name)
        return False


def user_story_21_b(indi, wifeid, name):
    '''
    Correct gender role for wife
    indi is the dict of all individuals
    wifeid is the id of the wife
    name is the name of the wife
    '''

    wife_gender = indi[wifeid].gender

    if wife_gender == "F":
        return True
    else:
        print("ERROR: US21: Incorrect gender " + wife_gender + " for wife " + name)
        return False


def user_story_22(indi, idtag):
    '''
    Ensure only unique ids
    indi is the dict of all individuals
    '''

    if idtag in indi:
        print("ERROR: US22: Someone with the id: " + idtag + " already exists.")
        return False
    else:
        return True


def user_story_23(indi):
    '''
    No more than one individual with the same name and birth date should appear in a GEDCOM file
    indi is the dict of all individuals
    '''
    unique = list()

    for i in indi:
        unique.append((indi[i].name, indi[i].birth))
    if (len(unique) == len(set(unique))):
        return True
    else:
        print("ERROR: US23: Duplicates found in file, two people with the name name and birthdate")
        return False
    
#def familylist(indi, fam, family):
 #   familylist = list()
  #  familylist.append(fam[family].wifeid)
   # familylist.append(fam[family].husbid)
    #for child in fam[family].chil:
     #   familylist.append(indi[child].idtag)
            
    #return familylist
    
def user_story_25(indi, fam):
    '''
    No more than one child with the same name and birth date should appear in a family
    '''

    for family in fam:
        childlist = fam[family].chil
        for child in childlist:
            temp = childlist
            while len(temp) > 1:
                if indi[child].idtag == indi[temp[0]].idtag:
                    temp.pop(0)
                if indi[child].name == indi[temp[0]].name:
                    if indi[child].birth == indi[temp[0]].birth:
                        print("ERROR: US25: Duplicates found in file, two people with the same name and birthdate: " +
                              indi[child].name + " and " + indi[temp[0]].name + " have birthday of: " + indi[child].birth.strftime(
                            '%Y-%m-%d'))
                        return False
                else:
                    temp.pop(0)
    return True  


def user_story_29_helper(indi, idtag):
    '''
    Returns the idtags of people who are deceased
    indi is the dict of all individuals
    idtag is the current id tag of the person
    '''
    death_status = indi[idtag].death
    if death_status != 'NA':
        return idtag
    else:
        return None


def user_story_29(indi):
    '''
    Return a list of the deceased
    indi is the dict of all individuals
    '''
    deceased = []
    deceased_names = []
    for i in indi:
        temp = user_story_29_helper(indi, i)
        if temp:
            deceased.append(temp)
            deceased_names.append(indi[temp].name)
    print("US29: List of all deceased people in the GEDCOM file: " + str(deceased_names))
    return deceased


def user_story_30_helper(indi, i, fam):
    for f in fam:
        if fam[f].husbid == i or fam[f].wifeid == i:
            if fam[f].div == "NA":
                if indi[i].death == "NA":
                    return True


def user_story_30(indi, fam):
    '''
    List all living married people in a GEDCOM file
    indi is the dict of all individuals
    fam is the dict of all families
    '''
    married = []
    married_names = []
    for i in indi:
        if user_story_30_helper(indi, i, fam):
            married.append(i)
            married_names.append(indi[i].name)
    print("US30: List of all living married people in the GEDCOM file: " + str(married_names))
    return married


def user_story_34_helper(indi, fam, family):
    if fam[family].marr != "NA" and indi[fam[family].wifeid].birth != "NA" and indi[fam[family].husbid].birth != "NA":
        wife_age_married = calc_difference(indi[fam[family].wifeid].birth, fam[family].marr)
        husb_age_married = calc_difference(indi[fam[family].husbid].birth, fam[family].marr)

        if husb_age_married < 0 or wife_age_married < 0:
            return False
        if husb_age_married > wife_age_married * 2:
            #print("husb age: " + str(husb_age_married) + " wife age: " + str(wife_age_married))
            return True
        elif wife_age_married > husb_age_married * 2:
            #print("husb age: " + str(husb_age_married) + " wife age: " + str(wife_age_married))
            return True
        else:
            return False


def user_story_34(indi, fam):
    '''
    List all couples who were married when the older spouse was more than twice as old as the younger spouse
    indi is the dict of all individuals
    fam is the dict of all families
    '''

    married = []
    married_names = []
    for family in fam:
        if user_story_34_helper(indi, fam, family): 
            print("appending: " + fam[family].husbname + " and " + fam[family].wifename)
            married.append(fam[family].husbid)
            married.append(fam[family].wifeid)
            married_names.append(fam[family].husbname)
            married_names.append(fam[family].wifename)
    print(
        "US34: List of all living married people when the older spouse was more than twice as old as the younger spouse in the GEDCOM file: " + str(
            married_names))
    return married

def user_story_35_helper(indi, idtag):
    birthdays = indi[idtag].birth
    current_date = date.today()
    recent_dates = current_date - timedelta(days=30)
    if birthdays != "NA":
        if recent_dates <= birthdays <= current_date:
            return idtag
        else:
            return False
    return False


def user_story_35(indi):
    '''
    List all people in a GEDCOM file who were born in the last 30 days
    indi is the dict of all individuals in the file
    '''
    recent_births = []
    recent_births_names = []
    for i in indi:
        temp = user_story_35_helper(indi, i)
        if temp:
            recent_births.append(temp)
            recent_births_names.append(indi[temp].name)
    print("US35: List of all births in the past 30 days: " + str(recent_births_names))
    return recent_births


def user_story_36_helper(indi, idtag):
    death_days = indi[idtag].death
    current_date = date.today()
    recent_dates = current_date - timedelta(days=30)
    if death_days != 'NA':
        if recent_dates <= death_days <= current_date:
            return idtag
        else:
            return False
    else:
        return False


def user_story_36(indi):
    '''
    List all people in a GEDCOM file who died in the last 30 days
    indi is the dict of all individuals in the file
    '''
    recent_deaths = []
    recent_deaths_names = []
    for i in indi:
        temp = user_story_36_helper(indi, i)
        if temp:
            recent_deaths.append(temp)
            recent_deaths_names.append(indi[temp].name)
    print("US36: List of all deaths in the past 30 days: " + str(recent_deaths_names))
    return recent_deaths


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
        self.husbname = "NA"
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
                if user_story_22(indi, args):
                    person.idtag = args
                    indi[person.idtag] = person
                else:
                    newLine = arr[i].strip()
                    new_level, new_tag, new_args, new_tokens = validLine(newLine)

                    if new_tag == "NAME":
                        print("Not adding " + new_args + " to the table because their I.D. was already in use")

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

                    user_story_1(new_date)
                    person.birth = new_date
                    person.age = determine_age(new_date, datetime.datetime.today())

            elif tag == "DEAT":
                person.alive = False

                # need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)

                if new_tag == "DATE":
                    new_date = datetime.datetime.strptime(new_args, "%d %b %Y").date()

                    user_story_1(new_date)
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

                    user_story_1(new_date)
                    user_story_2(indi, new_date, family.husbid, family.wifeid)
                    user_story_11(indi, fam, family.husbid, family.wifeid)

                    family.marr = new_date

            elif tag == "DIV":

                # need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)

                if new_tag == "DATE":
                    new_date = datetime.datetime.strptime(new_args, "%d %b %Y").date()

                    user_story_1(new_date)

                    family.div = new_date

            elif tag == "HUSB":
                family.husbid = args
                family.husbname = indi[args].name

            elif tag == "WIFE":
                family.wifeid = args
                family.wifename = indi[args].name

            elif tag == "CHIL":
                family.chil.append(args)

    user_story_13(indi, fam)
    user_story_23(indi)
    user_story_25(indi, fam)
    user_story_29(indi)
    user_story_30(indi, fam)
    user_story_34(indi, fam)
    user_story_35(indi)
    user_story_36(indi)

    for famtag in fam:
        user_story_4(fam[famtag].marr, fam[famtag].div, fam[famtag].husbname, fam[famtag].wifename)
        user_story_5(fam[famtag].marr, fam[famtag].husbid, fam[famtag].wifeid, indi)
        user_story_6(fam[famtag].div, fam[famtag].husbid, fam[famtag].wifeid, indi)
        user_story_10(indi, famtag, fam)
        #user_story_11(indi, fam, fam[famtag].husbid, fam[famtag].wifeid)
        user_story_15(fam[famtag].chil, famtag)
        user_story_18(indi, fam[famtag].husbid, fam[famtag].wifeid)
        user_story_21_a(indi, fam[famtag].husbid, fam[famtag].husbname)
        user_story_21_b(indi, fam[famtag].wifeid, fam[famtag].wifename)

    for per in indi:
        user_story_3(indi[per].birth, indi[per].death, indi[per].name)
        user_story_7(indi[per].birth, indi[per].death, indi[per].name)

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
        # file = open('NicoleFamily.ged', 'r')
        # file = open('user_story_geds/us22.ged', 'r')

        #file = open('user_story_geds/bigged.ged', 'r')
        file = open('user_story_geds/us25.ged')
    except OSError:
        print("Cannot open file")

    indi_info, fam_info = create_tables(file)

    create_indi(indi_info)
    create_fam(fam_info)

    file.close()


if __name__ == '__main__':
    main()
