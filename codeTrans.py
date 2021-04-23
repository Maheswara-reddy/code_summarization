import re 
from lexPython import lexer

# Erasing the previous contenet in file 
file = open("myfile.txt","r+")
file.truncate(0)
file.close()

# To check the Identifiiers in the line 
regex = '^[A-Za-z_][A-Za-z0-9_]*'

# Function to check the attributes given to variables
def checkdotoperator(words):
    retStatement = ""
    for i in words:
        k = i.find(".")
        if k > 0 :
            c = re.split(r'\s+', re.sub(r'[.\,]', ' ', i).strip())
            retStatement = "The attribute " + c[0] + " is applied on " + c[1] + ". "
        else:
            retStatement = ""
    return retStatement

# Tranlating the if loop
def ifloop(line, code_list):
    words = re.split(r'\s+', re.sub(r'[(\)\:]', ' ', line).strip())
    ret = ""
    reto = ""
    retStatement = ""
    index = 1
    if any(x in words for x in code_list):
        reto = x + "is an identifer"
    for i in words:
        if(i == '=='):
            ret = "equality"
            index = words.index('==')
            retStatement = checkdotoperator(words)
        if(i == '!='):
            ret = "inequality"
            index = words.index('!=')
            retStatement = checkdotoperator(words)
        if(i == ">="):
            ret = "greater than or equal"
            index = words.index('>=')
            retStatement = checkdotoperator(words)
        if(i == ">"):
            ret = "greater than"
            index = words.index('>')
            retStatement = checkdotoperator(words)
        if(i == "<="):
            ret = "less than or equal"
            index = words.index('<=')
            retStatement = checkdotoperator(words)
        if(i == "<"):
            ret = "less than"
            index = words.index('<')
            retStatement = checkdotoperator(words)
        if(i == "in"):
            ret = "if it exists in"
            index = words.index('in')
            retStatement = checkdotoperator(words)
    if(len(retStatement) > 0) :
        writestatement = "Here there is an if loop that checks " + ret + " condition between " + words[index-1]+ " and " + words[index+1] + retStatement + ". "
    else:
        writestatement = "Here there is an if loop that checks " + ret + " condition between " + words[index-1]+ " and " + words[index+1] + ". "
    
    return writestatement

# Translating the elif condition of the if loop
def elifloop(line, code_list):
    words = re.split(r'\s+', re.sub(r'[(\)\:]', ' ', line).strip())
    ret = ""
    retStatement = ""
    index = 1
    reto = ""
    if any(x in words for x in code_list):
        reto = x + "is an identifer"
    for i in words:
        if(i == '=='):
            ret = "equality"
            index = words.index('==')
            retStatement = checkdotoperator(words)
        if(i == '!='):
            ret = "inequality"
            index = words.index('!=')
            retStatement = checkdotoperator(words)
        if(i == ">="):
            ret = "greater than or equal"
            index = words.index('>=')
            retStatement = checkdotoperator(words)
        if(i == ">"):
            ret = "greater than"
            index = words.index('>')
            retStatement = checkdotoperator(words)
        if(i == "<="):
            ret = "less than or equal"
            index = words.index('<=')
            retStatement = checkdotoperator(words)
        if(i == "<"):
            ret = "less than"
            index = words.index('<')
            retStatement = checkdotoperator(words)
        if(i == "in"):
            ret = "if it exists in"
            index = words.index('in')
            retStatement = checkdotoperator(words)
    
    if(len(retStatement) > 0) :
        writestatement = " This is the elif condition of the if loop that checks " + ret + " condition between " + words[index-1]+ " and " + words[index+1] + retStatement + ". "
    else:
        writestatement = " Here there is an if loop that checks " + ret + " condition between " + words[index-1]+ " and " + words[index+1] + ". "
    
    return writestatement

# Tranlating the while loops
def whileloop(line, code_list):
    words = re.split(r'\s+', re.sub(r'[(\)\:]', ' ', line).strip())
    ret = ""
    retStatement = ""
    index = 1
    reto = ""
    if any(x in words for x in code_list):
        reto = x + "is an identifer"
    for i in words:
        if(i == '=='):
            ret = "equality"
            index = words.index('==')
            retStatement = checkdotoperator(words)
        if(i == '!='):
            ret = "inequality"
            index = words.index('!=')
            retStatement = checkdotoperator(words)
        if(i == ">="):
            ret = "greater than or equal"
            index = words.index('>=')
            retStatement = checkdotoperator(words)
        if(i == ">"):
            ret = "greater than"
            index = words.index('>')
            retStatement = checkdotoperator(words)
        if(i == "<="):
            ret = "less than or equal"
            index = words.index('<=')
            retStatement = checkdotoperator(words)
        if(i == "<"):
            ret = "less than"
            index = words.index('<')
            f = open("myfile.txt","a")
    retStatement = checkdotoperator(words)
    if(i == "in"):
        ret = "if it exists in"
        index = words.index('in')
        retStatement = checkdotoperator(words)

    if(len(retStatement) > 0) :
        writestatement = "A conditional while statement that satisfies the condition " + ret + " between " + words[index-1] + " and " + words[index+1]  + retStatement + ". "
    else:
        writestatement = "A conditional while statement that satisfies the condition " + ret + " between " + words[index-1] + " and " + words[index+1] + ". "

    return writestatement

# Trnslating the grammer if + , - , / , * , % operators exists
def operatorscheck(line):
    retStatement = ""
    # + operator
    x = line.find('+')
    if x > 0 :
        s = line.split('+')
        retStatement = "We are adding " +s[0]+ " and " + s[1] + ". "

    # - operator
    x = line.find('-')
    if x > 0 :
        s = line.split('-')
        retStatement = "We are subtracting " +s[1]+ " from "  + s[0] + ". "
    
    # * operator
    w = line.find('*')
    
    if w > 0 :
        s = line.split('*')
        retStatement = "We are subtracting " +s[1]+ " and " + s[0] + ". "

    # / operator
    w = line.find('/')
    if w > 0 :
        s = line.split('/')
        retStatement = "We are dividing " +s[1]+ " by " + s[0] + ". "
    
    # % operator
    w = line.find('%')
    if w > 0 :
        s = line.split('%')
        retStatement = "We are finding the remainder of " +s[1]+ " with " + s[0] + ". "

    return retStatement


# Translating the whole code line by line
def codetranslation(line, code_list):
    
    
    # Importing libraries.
    x = line.find("import")
    if x > 0:
        f = open("myfile.txt", "a")
        writestatement = "Imported an inbult library "+ line.split(' ')[x+1]+ ". "
        f.write(writestatement)

    # Functions
    x = line.find("def")
    if x > 0:
        s = line.split(' ')
        stri = "We have defined a function named "+ s[x+1] + "with input variables. "
        re.split('( | ) |',s[x+1])
        writestatement = stri + s[x+1][0]
        f = open("myfile.txt", "a")
        f.write(writestatement)
    
    # for loop
    x = line.find('for')
    y = line.find('#')
    if x > 0 and y < 0:
        words = re.split(r'\s+', re.sub(r'[(\)\:]', ' ', line).strip())
        index = -1
        for i in words:
            if i == 'range':
                index = words.index('range')
        if index > 0 :
            str = "Here we are iterating the for loop for the values in the range of " + words[index+1] +". "
        else :
            str = "We are iterating the for loop in " + words[3] + ". "
        writestatement = str + ". " 
        f = open("myfile.txt", "a")
        f.write(writestatement)
    
    # while loop
    x = line.find('while')
    y = line.find('#')
    if x > 0 and y < 0:
        writestatement = whileloop(line, code_list)
        f = open("myfile.txt","a")
        f.write(writestatement)
    
    # if loop
    x = line.find('if')
    y = line.find('#')
    if x > 0 and y < 0:
        writestatement = ifloop(line, code_list)
        f = open("myfile.txt","a")
        f.write(writestatement)

    # elif condition
    x = line.find('elif')
    y = line.find('#')
    if x > 0 and y < 0:
        writestatement = elifloop(line, code_list)
        f = open("myfile.txt","a")
        f.write(writestatement)
    
    # else condition
    x = line.find('else') 
    if x > 0:
        writestatement = "We have a else statement for the above if loop here. "
        f = open("myfile.txt", "a")
        f.write(writestatement)
    
    # return statement
    x = line.find('return')
    y = line.find('#') 
    if x > 0 and y < 0:
        s = line.split(' ')
        writestatement = "We are returning the value of " +s[x+1]+ " from this function" + ". "
        f = open("myfile.txt", "a")
        f.write(writestatement)

    # Lines involving operations outside if, while and for loops
    x = line.find("=")
    y = line.find("if")
    z = line.find("elif")
    w = line.find("while")
    v = line.find("#")
    ee = line.find("==")
    ei = line.find("+=")
    ed = line.find("-=")
    if x > 0 and y<0 and z<0 and w<0 and v<0 and ee<0 and ei < 0 and ed < 0:
        reti = ""
        reto = ""
        words = re.split(r'\s+', re.sub(r'[ ]', ' ', line).strip()) 
        index = words.index("=")
        i = words[index-1].find(".")
        j = words[index+1].find(".")
        op = ["+","-","*","/","%"]
        if any(x in words[index-1] for x in op):
            reto = operatorscheck(words[index-1])
            
        str1 = "Here we are equating " + words[index-1] +" and "+ words[index+1] + " values. " 
        if i > 0:
            c = re.split(r'\s+', re.sub(r'[.\,]', ' ', words[index-1]).strip())
            reti = " The attribute " + c[1] + " is applied on " + c[0] + " "
        if j > 0:
            c = re.split(r'\s+', re.sub(r'[.\,]', ' ', words[index+1]).strip())
            reti = " The attribute " + c[1] + " is applied on " + c[0] + ". "
        
        str1 = str1 + reti + reto
        writestatement = str1
        f = open("myfile.txt", "a")
        f.write(writestatement)
    
    # Incrementing the variable value
    x = line.find("+=")
    y = line.find("if")
    z = line.find("elif")
    w = line.find("while")
    v = line.find("#")
    ee = line.find("==")
    if x > 0 and y<0 and z<0 and w<0 and v<0 and ee<0:
        words = re.split(r'\s+', re.sub(r'[ ]', ' ', line).strip()) 

        index = words.index("+=")
        str1 = "We are increamenting the value of " + words[index-1] + " by " + words[index+1] + ". "
        writestatement = str1
        f = open("myfile.txt", "a")
        f.write(writestatement)


    # Decreamenting the variable value
    x = line.find("-=")
    y = line.find("if")
    z = line.find("elif")
    w = line.find("while")
    v = line.find("#")
    ee = line.find("==")
    if x > 0 and y<0 and z<0 and w<0 and v<0 and ee<0:
        words = re.split(r'\s+', re.sub(r'[ ]', ' ', line).strip()) 

        index = words.index("-=")
        str1 = "We are decreamenting the value of " + words[index-1] + " by " + words[index+1] + ". "
        writestatement = str1
        f = open("myfile.txt", "a")
        f.write(writestatement)
        
    # print function
    x = line.find("print")
    y = line.find("#")
    if x > 0 and y < 0:
        sta = ""
        k = lexer("Test1.py")
        words = re.split(r'\s+', re.sub(r'[(\)\+]', ' ', line).strip())
        words.remove('print')
        for i in words:
            sta = sta + i
        f = open("myfile.txt", "a")
        writestatement = "We are using print function to print the statement: " + sta + ". "
        f.write(writestatement)

    # commets in the program
    x = line.find("#")
    if x > 0 :
        line  = line.replace('#','')
        f = open("myfile.txt", "a")
        writestatement = "Comment" + line + ". "
        f.write(writestatement)

 
        f.close()

s = input() 
file1 = open(s, 'r')

Lines = file1.readlines()
code_list = lexer(s)
for line in Lines:
    line = " " + line
    codetranslation(line, code_list)

