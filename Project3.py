"""
@author: Michayla Ben-Ezra
@author: Nicole Hilden
@author: Caroline Telma
@author: Elena Sanchez
SSW555 - project 3

I pledge my honor that I have abided by the Stevens Honor System
-Michayla Ben-Ezra 9/10/2018

"""


#the dictionary below defines all of the levels and their valid tags for GEDCOM family trees
valid = {
    '0': ['HEAD', 'TRLR', 'NOTE'],
    '1': ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],
    '2': ['DATE']
    }

def validLine(line):
    
    #this prints each line in the file, strips it of the white space, splits the line up into any array called "tokens"
    #and then the array is used to identify the level, tag, and any associated arugments for the line
    #for line in file:
        line = line.strip()
        #print ('-->', line)
        tokens = line.split()
        level = tokens[0]
        tag = tokens[1]
        args = " ".join(tokens[2:])
    
        #this if statement is to decide if the line is valid or invalid
        #this decision is made by seeing if the tag in the line is at the appropriate level
        #if level in valid:
        
        if level in valid and tag in valid[level]:
            #print (level)
            #print (tag)
            ok = 'Y'
        else:
            if len(tokens)>= 3 and tokens[2] in ['INDI', 'FAM']:
                ok = 'Y'
            else:
                ok = 'N'

        return ok
                
def parseFile(file):
    #testValidFile = file
    #ok = validFile(testValidFile)
    
    for line in file:
        ok = validLine(line)
        line = line.strip()
        print ('-->', line)
        tokens = line.split()
        level = tokens[0]
        tag = tokens[1]
        args = " ".join(tokens[2:])
        
        #print ('-->', line)
    
        if len(tokens) >= 3:
            if tokens[2] in ['INDI', 'FAM']:
                print("<-- {}|{}|{}|{}".format(level, args, ok, tag))
            else:
                print("<-- {}|{}|{}|{}".format(level, tag, ok, args))
                    
        #to print the output if len<3
        else:
            if args == "":
                args = 'N/A'
            print ("<-- " + level.strip()+ "|"+ tag+"|"+ok+"|"+args)

                            
def main():
    #the line below opens the indicated file and reads it
    try:
        #file = open('/Users/Mbenezra/SSW-555/proj02test (1).ged', 'r')
        file = open('/Users/Test/Documents/SSW555/proj02test.ged')
    except:
        print("Cannot open file")
        
    parseFile(file)
    
if __name__ == '__main__':
    main()
        
        
