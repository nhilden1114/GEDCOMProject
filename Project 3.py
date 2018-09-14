"""
@author: Michayla Ben-Ezra
SSW555 - project 2

I pledge my honor that I have abided by the Stevens Honor System
-Michayla Ben-Ezra 9/10/2018

"""
#the line below opens the indicated file and reads it
file = open('/Users/Mbenezra/SSW-555/proj02test (1).ged', 'r')

#the dictionary below defines all of the levels and their valid tags for GEDCOM family trees
valid = {
    '0': ['HEAD', 'TRLR', 'NOTE'],
    '1': ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],
    '2': ['DATE']
    }

#this prints each line in the file, strips it of the white space, splits the line up into any array called "tokens"
#and then the array is used to identify the level, tag, and any associated arugments for the line
for line in file:
    print ('-->', line)
    line = line.strip()
    tokens = line.split()
    level = tokens[0]
    tag = tokens[1]
    args = " ".join(tokens[2:])

    #this if statement is to decide if the line is valid or invalid
    #this decision is made by seeing if the tag in the line is at the appropriate level
    #if level in valid:
    if tag in valid[level]:
        ok = 'y'
    else:
        if len(tokens)>= 3 and tokens[2] in ['INDI', 'FAM']:
            ok = 'y'
        else:
            ok = 'n'
    #else:
       # level, tag, valid, args

    if len(tokens) >= 3:
        if tokens[2] in ['INDI', 'FAM']:
            print("<-- {}|{}|{}|{}".format(level, args, ok, tag))
        elif valid:
            print("<-- {}|{}|{}|{}".format(level, tag, ok, args))
        else:
            print("<-- {}|{}|{}|{}".format(level, tag, ok, args))

    #to print the output
    #print ("<--", "|", level, "|", ok, "|",  tag, "|", args)