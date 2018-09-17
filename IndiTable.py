from Project3 import validLine
from prettytable import PrettyTable

import datetime


def determineAge(dob, currDate):
    
    birth = datetime.datetime.strptime(dob, "%d %b %Y").date()
    age = currDate.year - birth.year - ((birth.month, birth.day) > (currDate.month, currDate.day))
    return age

def createIndiTable(file):

    tab = PrettyTable()
    tab.field_names = ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]

    for line in file:
        ok = validLine(line)
        line = line.strip()
        tokens = line.split()
        level = tokens[0]
        tag = tokens[1]
        args = " ".join(tokens[2:])

        #needs to be initialized somewhere else
        #ID,Name,Gender,Birthday,Age,Alive,Death,Child,Spouse = ("","","","","","","","","")

        if ok == "Y" and (tag in ["NAME","SEX","BIRTH","DEAT","FAMC","FAMS"] or (len(tokens)>=3 and tokens[2]=="INDI")):
                
            if tag == "NAME":
                Name = args
                
            elif tag == "SEX":
                Gender = args
                
            elif tag == "BIRT":
                
                #need to access next line for the DATE
                newLine = next(file)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(tokens[2:])
                if newTag == "DATE":
                    Birthday = newArgs
                    Age = determineAge(newArgs, datetime.date.today())

            elif tag == "DEAT":
                Alive = "False"

                #need to access next line for the DATE
                newLine = next(file)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(tokens[2:])
                if newTag == "DATE":
                    Death = newArgs
                    Age = determineAge(Birthday, newArgs)

            elif tag == "FAMS":
                Spouse = args
                
            elif tag == "FAMC":
                Child = args

            elif tokens[2] == "INDI":
                ID = tokens[1]


        try: (ID,Name,Gender,Birthday,Age,Alive,Death,Child,Spouse)
        except: continue

        tab.add_row([ID,Name,Gender,Birthday,Age,Alive,Death,Child,Spouse])
            
    return tab

def main():

    try:
        file = open('/Users/Test/Documents/SSW555/proj02test.ged')
    except:
        print("Cannot open file")
        
    print(createIndiTable(file)  )
    #print(determineAge("14 NOV 1997"))
    
if __name__ == '__main__':
    main()
        

