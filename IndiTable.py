from Project3 import validLine
from prettytable import PrettyTable

import datetime


def determineAge(dob, date):
    
    #currDate = datetime.datetime.strptime(date, "%d %b %Y").date()
    #birth = datetime.datetime.strptime(dob, "%d %b %Y").date()
    age = currDate.year - birth.year - ((birth.month, birth.day) > (currDate.month, currDate.day))
    if age <0:
        return age*(-1)
    return age

def createIndiTable(file):

    tab = PrettyTable()
    tab.field_names = ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]

    #vals = dict({"ID":"N/A","Name":"N/A","Gender":"N/A","Birthday":"N/A","Age":"N/A","Alive":"True","Death":"N/A","Child":"N/A","Spouse":"N/A"})
    individual = dict()

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

        if(len(tokens)>=3 and tokens[2] = "INDI"):
            individual["ID"] = tokens[1]
            

        if ok == "Y" and (tag in ["NAME","SEX","BIRT","DEAT","FAMC","FAMS"] ): #or (len(tokens)>=3 and tokens[2]=="INDI")):
                
            if tag in ["NAME","SEX"]:
                #vals["Name"] = args
                curr_indi[tag] = args
                
            #elif tag == "SEX":
             #   vals["Gender"] = args

            elif tag == "BIRT":
                
                #need to access next line for the DATE
                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "DATE":
                    #vals["Birthday"] = newArgs
                    curr_indi["Birthday"] = datetime.datetime.strptime(newArgs, "%d %b %Y").date()
                    #vals["Age"] = determineAge(newArgs, "17 NOV 2018")
                    curr_indi["Age"] = determineAge(curr_indi["Birthday"], datetime.date.today())

            elif tag == "DEAT":
                #vals["Alive"] = "False"
                curr_indi["Alive"] = "False"
                
                #need to access next line for the DATE
                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "DATE":
                    #vals["Death"] = newArgs
                    newDate = datetime.datetime.strptime(newArgs, "%d %b %Y").date()
                    curr_indi["Death"] = newDate
                    #vals["Age"] = determineAge(vals["Birthday"], newArgs)
                    curr_indi["Age"] = determineAge(curr_indi["Birthday"], newDate)


            elif tag == "FAMS":
                vals["Spouse"] = args

                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                if newOK == "Y" and newTag == "FAMC":
                    vals["Child"] = newArgs
                    tab.add_row([vals["ID"],vals["Name"],vals["Gender"],vals["Birthday"],vals["Age"],vals["Alive"],vals["Death"],vals["Child"],vals["Spouse"]])
                    i=i+1
                else:
                    vals["Child"] = "N/A"
                    tab.add_row([vals["ID"],vals["Name"],vals["Gender"],vals["Birthday"],vals["Age"],vals["Alive"],vals["Death"],vals["Child"],vals["Spouse"]])
                    vals["Alive"] = "True"
                    vals["Death"] = "N/A"
                
            elif tag == "FAMC":
                vals["Child"] = args
                vals["Spouse"] = "N/A"
                tab.add_row([vals["ID"],vals["Name"],vals["Gender"],vals["Birthday"],vals["Age"],vals["Alive"],vals["Death"],vals["Child"],vals["Spouse"]])
                vals["Alive"] = "True"
                vals["Death"] = "N/A"

            elif tokens[2] == "INDI":
                vals["ID"] = tokens[1]
            
    return tab

def main():

    try:
        file = open('/Users/Test/Documents/SSW555/NicoleFamily.ged')
    except:
        print("Cannot open file")
        
    print(createIndiTable(file)  )
    #print(determineAge("14 NOV 1997"))
    
if __name__ == '__main__':
    main()
        

