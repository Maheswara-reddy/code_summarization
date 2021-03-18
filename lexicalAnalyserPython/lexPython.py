import re

s = input("Please enter a Python file : ")
f = open(s, 'r')
text = f.read()

symbols = ['!', '@', '#', '$', '%', '&', '^', '*']
oparators = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
delimiters = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']
keywords = ['False','await','else', 'else:','import','pass','None','break','except','in','raise','True','class','finally','is','return','and','continue','for','lambda','try','as','def','from','nonlocal','while','assert','del','global','not','with','async','elif','if','or','yield']

keyword = []
identifier = []
constant = []

tokens = []
stringCheck = False
wordCheck = False
commentCheck = False
token = ''

for i in text:
	if i == '#':
    		commentCheck = True

	elif commentCheck == True :
		if i == '\n':
			token = ''
			commentCheck = False
	
	elif i == '"' or i == "'":
		if stringCheck:
			tokens.append(token)
			token = ''
		stringCheck = not stringCheck

	elif stringCheck == True:
		token = token+i
    
	elif i in symbols:
		tokens.append(i)
           
	elif i.isalnum() and wordCheck == False:
		wordCheck = True
		token = i
    
	elif (i in delimiters) or (i in oparators):
		if token:
			tokens.append(token)
			token = ''
        
		if not (i==' ' or i=='\n' or i=='	'):
			tokens.append(i)

	elif wordCheck:
		token = token+i


for token in tokens:
	if token in keywords:
		keyword.append(token)
				
	elif re.search("^[a-zA-Z][a-zA-Z]*$",token):
		identifier.append(token)
							 
print("No. of keywords =  ", len(keyword))
print(keyword)
print("\nNo. of identifiers =  ",len(identifier))
print(identifier)
f.close()   
