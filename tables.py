from prettytable import PrettyTable
import datetime
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


def user_story_1(inputDate):  # Dates (birth, marriage, divorce, death) should not be after the current date

    current = datetime.datetime.today()

    difference = current.year - inputDate.year - ((inputDate.month, inputDate.day) > (current.month, current.day))

    if difference < 0:
        print ("ERROR: US01: Date: " + inputDate.strftime('%Y-%m-%d') + " should not be after the current one")
        return False
    else:
        return True


def user_story_2(indi, marr_date, husbid, wifeid):  # Birth should occur before marriage of an individual
    husb_birth = indi[husbid].birth
    wife_birth = indi[wifeid].birth

    wife_diff = marr_date.year - wife_birth.year - ((wife_birth.month, wife_birth.day) > (marr_date.month, marr_date.day))
    husb_diff = marr_date.year - husb_birth.year - ((husb_birth.month, husb_birth.day) > (marr_date.month, marr_date.day))

    if wife_diff < 0:
        print("ERROR: US02: Marriage date of " + marr_date.strftime('%Y-%m-%d') + " cannot be before Birth date of " + indi[wifeid].name)
        return False
    if husb_diff < 0:
        print("ERROR: US02: Marriage date of " + marr_date.strftime('%Y-%m-%d') + " cannot be before Birth date of " + indi[husbid].name)
        return False
    else:
        return True


def user_story_3(birthday, death_day): # a person's birthday must be before their death date

    difference = death_day.year - birthday.year - ((birthday.month, birthday.day) > (death_day.month, death_day.day))

    if birthday != "NA" and birthday < datetime.datetime.today():
        if death_day != "NA" and death_day <= datetime.datetime.today():
            if difference < 0:
                print("ERROR: US03: Death date of " + death_day.strftime('%Y-%m-%d') + " should not be before their birth date of " + birthday.strftime('%Y-%m-%d'))
                return False
            else:
                return True
        else:
            print("ERROR: US03: Death date of " + death_day.strftime('%Y-%m-%d') + " not valid")
            return False
    else:
        print("ERROR: US03: Birth date of " + birthday.strftime('%Y-%m-%d') + " not valid")
        return False


def user_story_4(marriage_date, divorce_date):

    difference = divorce_date.year - marriage_date.year - ((marriage_date.month, marriage_date.day) > (divorce_date.month, divorce_date.day))

    if marriage_date != "NA" and marriage_date < datetime.datetime.today():
        if divorce_date != "NA" and divorce_date <= datetime.datetime.today():
            if difference < 0:
                print("ERROR: US04: Divorce date should not be before the marriage date")
                return False
            else:
                return True
        else:
            print("ERROR: US04: Divorce date not valid")
            return False
    else:
        print("ERROR: US04: Marriage date not valid")
        return False


def user_story_5(marriage_date, death_date):  # A person cannot get married after their death date

    difference = death_date.year - marriage_date.year - ((marriage_date.month, marriage_date.day) > (death_date.month, death_date.day))

    if marriage_date != "NA" and marriage_date < datetime.datetime.today():
        if death_date != "NA" and death_date <= datetime.datetime.today():
            if difference < 0:
                print("ERROR: US05: Marriage date of " + marriage_date.strftime('%Y-%m-%d') +
                      " should not occur after death date of " + death_date.strftime('%Y-%m-%d'))
                return False
            else:
                return True
        else:
            print("ERROR: US05: Death date of " + death_date.strftime('%Y-%m-%d') + " not valid")
            return False
    else:
        print("ERROR: US05: Marriage date of " + marriage_date.strftime('%Y-%m-%d') + " not valid")
        return False


def user_story_6(divorce_date, death_date):  # A person cannot get a divorce after death

    difference = death_date.year - divorce_date.year - ((divorce_date.month, divorce_date.day) > (death_date.month, death_date.day))

    if divorce_date != "NA" and divorce_date < datetime.datetime.today():
        if death_date != "NA" and death_date <= datetime.datetime.today():
            if difference < 0:
                print("ERROR: US06: Divorce date should not occur after death date")
                return False
            else:
                return True
        else:
            print("ERROR: US06: Death date not valid")
            return False
    else:
        print("ERROR: US06: Divorce date not valid")
        return False


def user_story_18(indi, husbid, wifeid): # Siblings should NOT marry
    husb_fam = indi[husbid].famc
    wife_fam = indi[wifeid].famc
    if husb_fam == wife_fam:
        print("ERROR: US18: Incest occurring with " + str(indi[husbid].idtag) + " and " + str(indi[wifeid].idtag))
        return False
    else:
        return True


def user_story_21_a(indi, husbid):  # Correct gender role for husband
    husb_gender = indi[husbid].gender

    if husb_gender == "M":
        return True
    else:
        print("ERROR: US21: Incorrect gender " + husb_gender + " for husband")
        return False


def user_story_21_b(indi, wifeid):  # Correct gender role for wife
    wife_gender = indi[wifeid].gender

    if wife_gender == "F":
        return True
    else:
        print("ERROR: US21: Incorrect gender " + wife_gender + " for wife")
        return False


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

    indi = dict() # indi[id] = instance of class Person
    fam = dict() # fam[id] = instance of class Family

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
                    if user_story_1(new_date):
                        person.birth = new_date
                        person.age = determine_age(new_date, datetime.datetime.today())

            elif tag == "DEAT":
                person.alive = False
                
                # need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)
                
                if new_tag == "DATE":
                    new_date = datetime.datetime.strptime(new_args, "%d %b %Y").date()
                    if user_story_1(new_date):
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
                    if user_story_1(new_date):
                        if user_story_2(indi, new_date, family.husbid, family.wifeid):
                            family.marr = new_date

            elif tag == "DIV":

                # need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)
                
                if new_tag == "DATE":
                    new_date = datetime.datetime.strptime(new_args, "%d %b %Y").date()
                    if user_story_1(new_date):
                        family.div = new_date

            elif tag == "HUSB":
                family.husbid = args
                family.husbname = indi[args].name

            elif tag == "WIFE":
                family.wifeid = args
                family.wifename = indi[args].name

            elif tag == "CHIL":
                family.chil.append(args)
                
    """for key in fam:
        user_story_18(indi, fam[key].husbid, fam[key].wifeid)"""
        
    create_indi(indi)
    create_fam(fam)


def create_indi(indi):
    
    table = PrettyTable()
    table.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age','Alive', 'Death', 'Child', 'Spouse']

    # print(indi)
    
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
        # file = open('/Users/Test/Documents/SSW555/NicoleFamily.ged')
        # file = open ('/Users/carolinetelma/Desktop/NicoleFamily.ged', 'r')
        file = open('C:/Users/Mbenezra/SSW-555/GEDCOMProject/NicoleFamily.ged', 'r')
    except FileNotFoundError:
        print("Cannot open file")

    print(create_tables(file))


if __name__ == '__main__':
    main()
        

