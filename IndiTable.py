from Project3 import validLine
from prettytable import PrettyTable

import datetime


def determineAge(dob, currDate):
    
    birth = datetime.datetime.strptime(dob, "%d %b %Y").date()
    age = currDate.year - birth.year - ((birth.month, birth.day) > (currDate.month, currDate.day))
    if age <0:
        return age*(-1)
    return age

def createIndiTable(file):

    tab = PrettyTable()
    tab.field_names = ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]

    vals = dict({"ID":"N/A","Name":"N/A","Gender":"N/A","Birthday":"N/A","Age":"N/A","Alive":"N/A","Death":"N/A","Child":"N/A","Spouse":"N/A"})

    for line in file:
        ok = validLine(line)
        line = line.strip()
        tokens = line.split()
        level = tokens[0]
        tag = tokens[1]
        args = " ".join(tokens[2:])

        #needs to be initialized somewhere else
        #ID,Name,Gender,Birthday,Age,Alive,Death,Child,Spouse = ("","","","","","","","","")

        if ok == "Y" and (tag in ["NAME","SEX","FAMC","FAMS"] or (len(tokens)>=3 and tokens[2]=="INDI")):
                
            if tag == "NAME":
                vals["Name"] = args
                
            elif tag == "SEX":
                vals["Gender"] = args

 #           elif tag == "BIRT":
                
                #need to access next line for the DATE
 #               newLine = next(file)
  #              newTok = newLine.split()
   #             newTag = newTok[1]
    #            newArgs = " ".join(tokens[2:])
     #           if newTag == "DATE":
      #              vals["Birthday"] = newArgs
       #             vals["Age"] = determineAge(newArgs, datetime.date.today())

        #    elif tag == "DEAT":
         #       vals["Alive"] = "False"

                #need to access next line for the DATE
          #      newLine = next(file)
           #     newTok = newLine.split()
            #    newTag = newTok[1]
             #   newArgs = " ".join(tokens[2:])
              #  if newTag == "DATE":
                #     vals["Death"] = newArgs
                 #   vals["Age"] = determineAge(vals["Birthday"], newArgs)

            elif tag == "FAMS":
                vals["Spouse"] = args
                vals["Child"] = "N/A"
                tab.add_row([vals["ID"],vals["Name"],vals["Gender"],vals["Birthday"],vals["Age"],vals["Alive"],vals["Death"],vals["Child"],vals["Spouse"]])

                
            elif tag == "FAMC":
                vals["Child"] = args
                vals["Spouse"] = "N/A"
                tab.add_row([vals["ID"],vals["Name"],vals["Gender"],vals["Birthday"],vals["Age"],vals["Alive"],vals["Death"],vals["Child"],vals["Spouse"]])


            elif tokens[2] == "INDI":
                vals["ID"] = tokens[1]

        elif ok == "Y" and tag == "DATE":
            vals["Age"] = determineAge(args, datetime.date.today())
            print(args, " and ", vals["Age"] )




        #try: (ID,Name,Gender,Birthday,Age,Alive,Death,Child,Spouse)
        #except: continue

        #tab.add_row([ID,Name,Gender,Birthday,Age,Alive,Death,Child,Spouse])
            
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
        

