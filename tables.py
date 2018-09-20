from prettytable import PrettyTable
import datetime
from Project3 import validLine

def determineAge(dob, date):

    '''Calculate the age of a person given two dates'''
    
    currDate = datetime.datetime.strptime(date, "%d %b %Y").date()
    birth = datetime.datetime.strptime(dob, "%d %b %Y").date()
    age = currDate.year - birth.year - ((birth.month, birth.day) > (currDate.month, currDate.day))
    return age

class Person():
    
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

class Family():

    def __init__(self):
        self.idtag = "NA"
        self.marr = "NA"
        self.div = "N/A"
        self.husbid = "NA"
        self.husbnam = "NA" 
        self.wifeid = "NA"
        self.wifename = "NA"
        self.chil = list()

def createTables(file):

    indi = dict() # indi[id] = instance of class Person
    fam = dict() # fam[id] = instance of class Family

    arr = file.readlines()

    i = 0
    person = None
    family = None

    while  i < len(arr):
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
                
                #need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)
                
                if new_tag == "DATE":
                    person.birth = new_args
                    person.age = determineAge(new_args, "19 SEP 2018")

            elif tag == "DEAT":
                person.alive = False
                
                #need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)
                
                if new_tag == "DATE":
                    person.death = new_args
                    person.age = determineAge(person.birth, new_args)


            elif tag == "FAMS":
                person.fams.append(args)
                
            elif tag == "FAMC":
                person.famc.append(args)

            elif tag == "MARR":

                #need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)
                
                if new_tag == "DATE":
                    family.marr = new_args

            elif tag == "DIV":

                #need to access next line for the DATE
                newLine = arr[i].strip()
                new_level, new_tag, new_args, new_tokens = validLine(newLine)
                
                if new_tag == "DATE":
                    family.div = new_args

            elif tag == "HUSB":
                family.husbid = args
                family.husbname = indi[args].name

            elif tag == "WIFE":
                family.wifeid = args
                family.wifename = indi[args].name

            elif tag == "CHIL":
                family.chil.append(args)
                

    createINDI(indi)
    createFAM(fam)

def createINDI(indi):
    
    table = PrettyTable()
    table.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age','Alive', 'Death', 'Child', 'Spouse']
    
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
        
    print (table)

def createFAM(fam):
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
        
    print (table)
    
    
def main():

    try:
        file = open('/Users/Test/Documents/SSW555/NicoleFamily.ged')
    except:
        print("Cannot open file")
        
    print(createTables(file))
    
if __name__ == '__main__':
    main()
        

