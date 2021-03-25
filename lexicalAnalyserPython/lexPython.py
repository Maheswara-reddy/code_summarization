import re
import parser

s = input("Please enter a Python file : ")
f = open(s, 'r')
text = f.read()

def load_suite(source_string):
    st = parser.suite(source_string)
    return st, st.compile()

def load_expression(source_string):
    st = parser.expr(source_string)
    return st, st.compile()


symbols = ['!', '@', '#', '$', '%', '&', '^', '*']
oparators = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
delimiters = [' ', '	', '.', ',', '\n', ';',  '(', ')', '<', '>', '{', '}', '[', ']']
keywords = ['False', 'await', 'else', 'else:', 'import', 'pass', 'None', 'break', 'except', 'in', 'raise', 'True', 'class', 'finally', 'is', 'return', 'and','continue', 'for', 'lambda', 'try', 'as', 'def', 'from', 'nonlocal', 'while', 'assert', 'del', 'global', 'not', 'with', 'async', 'elif', 'if', 'or', 'yield', 're', 'elif', '']
inbuiltFunctions = ['abs','all','any','ascii','bin','bool','bytearray','bytes','callable','chr','classmethod','compile','complex','delattx','dict','divmod','enumarate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','memoryview','min','next','object','oct','open','ord','print','pow','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip','_import_','','','','',]
inbuiltLibrary = ['__future__','_abc','_ast ','_asyncio','_bisect ','_blake2','_bootlocale','_bz2','_codecs','_codecs_cn','_codecs_hk','_codecs_iso2022','_collections ','_compat_pickle','_compat_pickle','_contextvars','_csv ','_ctypes ','_datetime','abc','aifc','asyncore','calendar ','cgitb ','cmath','codecs','collections','copy','ctypes','dataclasses','dummy_threading','fileinput','fnmatch','getpass','gettext','hashlib','heapq','importlib','inspect','io','json','keyword','lib2to3','linecache','locale','modulefinder','re','math','random','numbers','ntpath','os','parser','pickle','pip','pprint','queue','selectors','smtplib','statistics','string','struct','symbol','sympyprinting','symtable','sys','tempfile','threading','token','tokenize','turtle','types','typing','unicodedata','warnings','webbrowser','xml','zipimport',]

tokens = []
stringCheck = False
wordCheck = False
commentCheck = False
token = ''

for i in text:
    if i == '#':
        commentCheck = True

    elif commentCheck == True:
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

        if not (i == ' ' or i == '\n' or i == '	'):
            tokens.append(i)

    elif wordCheck:
        token = token+i


code_list = []
lex_dictionary = {}

for token in tokens:
    if token in keywords:
        if token == 'def':
            code_list.append(lex_dictionary)
            lex_dictionary = {}
        lex_dictionary[token] = "keyword"

    elif token in inbuiltFunctions :
        lex_dictionary[token] = "InbuiltFunction"
    
    elif token in inbuiltLibrary :
        lex_dictionary[token] = "InbuiltLibrary"

    elif re.search("^[a-zA-Z][a-zA-Z]*$", token):
        lex_dictionary[token] = "Identifier"


code_list.append(lex_dictionary)

for i in code_list:
    print(i)