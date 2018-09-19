from prettytable import PrettyTable
import datetime
from Project3 import validLine

def determineAge(dob, date):
    
    currDate = datetime.datetime.strptime(date, "%d %b %Y").date()
    birth = datetime.datetime.strptime(dob, "%d %b %Y").date()
    age = currDate.year - birth.year - ((birth.month, birth.day) > (currDate.month, currDate.day))
    return age

class Person():

    idtag, name, gender, birth, age, alive, death, famc, fams = '','','','','','True','N/A',[],[]

class Family():

    idtag, marr, div, husbid, husbnam, wifeid, wifename, chil = '','','N/A','','','','',[]


def createTables(file):

    indi = dict()
    fam = dict()

    arr = []
    for line in file:
        arr.append(line.strip())

    i=0;
    while(i<len(arr)):
        line = arr[i]
        ok = validLine(line)
        tokens = line.split()
        level = tokens[0]
        tag = tokens[1]
        args = " ".join(tokens[2:])

        i+=1

        if ok == "Y" and (tag in ["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","CHIL","DIV","HUSB","WIFE"] or (len(tokens)>=3 and tokens[2] in ["INDI","FAM"])):
                
            if tag == "NAME":
                person.name = args
                
            elif tag == "SEX":
                person.gender = args

            elif tag == "BIRT":
                
                #need to access next line for the DATE
                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "DATE":
                    person.birth = newArgs
                    person.age = determineAge(newArgs, "17 SEP 2018")

            elif tag == "DEAT":
                person.alive = "False"
                
                #need to access next line for the DATE
                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "DATE":
                    person.death = newArgs
                    person.age = determineAge(person.birth, newArgs)


            elif tag == "FAMS":
                person.fams.append(args)
                
            elif tag == "FAMC":
                person.famc.append(args)

            elif tag == "MARR":
                
                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "DATE":
                    family.marr = newArgs

            elif tag == "DIV":
                
                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "DATE":
                    family.div = newArgs

            elif tag == "HUSB":
                family.husbid = args
                family.husbname = indi[args]

            elif tag == "WIFE":
                family.wifeid = args
                family.wifename = indi[args]

            elif tag == "CHIL":
                family.chil.append(args)

            elif tokens[2] == "INDI":
                person = Person()
                person.idtag = tokens[1]
                indi[person.idtag] = person
                person.famc = []
                person.fams = []
                
            elif tokens[2] == "FAM":
                family = Family()
                family.idtag = tokens[1]
                fam[family.idtag] = family
                family.chil = []
                

    createINDI(indi)
    createFAM(fam)

def createINDI(indi):
    
    table = PrettyTable()
    table.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age','Alive', 'Death', 'Child', 'Spouse']
    
    for key in indi:
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
    table.field_names = ['ID', 'Married', 'Divorced', 'Husband ID','Wife ID', 'Children']
    
    for key in fam:
        idt = fam[key].idtag
        mar = fam[key].marr
        div = fam[key].div
        hus = fam[key].husbname
        hid = fam[key].husbid
        wif = fam[key].wifename
        wid = fam[key].wifeid
        chi = fam[key].chil
        table.add_row([idt, mar, div, hid, wid, chi])
        
    print (table)
    
    
def main():

    try:
        file = open('/Users/Test/Documents/SSW555/NicoleFamily.ged')
    except:
        print("Cannot open file")
        
    print(createTables(file))
    
if __name__ == '__main__':
    main()
        

