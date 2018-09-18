from prettytable import PrettyTable
from Project3 import validLine


def createFamTable(file):

    tab = PrettyTable()
    tab.field_names = ["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"]

    vals = dict({"ID":"N/A","Married":"N/A","Divorced":"N/A","Husband ID":"N/A","Husband Name":"N/A","Wife ID":"N/A","Wife Name":"N/A","Children":"N/A"})

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

        if ok == "Y" and (tag in ["MARR","DIV"] or (len(tokens)>=3 and tokens[2] in ["INDI","FAM"])):

            if tag == "NAME":
                vals["Name"] = args

            elif tag == "MARR":
                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "DATE":
                    vals["Married"] = newArgs
        
            elif tag == "DIV":
                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "DATE":
                    vals["Divorced"] = newArgs

            #Need to somehow store all of the personal info somewhere
            #Like how to identify a husband or a wife based on the gender
            #Also, need to be able to list multiple children in the same family on the table

            #Should make a hash with the id as the key

            elif tokens[2] == "FAM":
                vals["ID"] = tokens[1]

            elif tokens[2] == "INDI":
                vals["Husband ID"] = tokens[1]

                newLine = arr[i]
                newOK = validLine(newLine)
                newTok = newLine.split()
                newTag = newTok[1]
                newArgs = " ".join(newTok[2:])
                
                if newOK == "Y" and newTag == "NAME":
                    vals["Husband Name"] = newArgs


        tab.add_row([vals["ID"],vals["Married"],vals["Divorced"],vals["Husband ID"],vals["Husband Name"],vals["Wife ID"],vals["Wife Name"],vals["Children"]])

    return tab
        

def main():

    try:
        file = open('/Users/Test/Documents/SSW555/NicoleFamily.ged')
    except:
        print("Cannot open file")
        
    print(createFamTable(file)  )
    
if __name__ == '__main__':
    main()
