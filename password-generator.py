import pyperclip as clip
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from subprocess import check_call


# params
numberChar = 16
includeSym = True
includeNum = True
includeLowercase = True
includeUppercase = True
excludeSameChar = True
excludeAmbiguousChar = True
AmbiguousChar = """{}[]()/\'"`~,;:.<>"""
sameChar = ['i','I','l','1','o','O','0']
autoCopy = True

# preparation stringsDB
stringsCollect = ''
if includeSym:
    stringsCollect += punctuation
if includeNum:
    stringsCollect += digits
if includeLowercase:
    stringsCollect += ascii_lowercase
if includeUppercase:
    stringsCollect += ascii_uppercase
if excludeSameChar:
    for char in sameChar:
        stringsCollect = stringsCollect.replace(char,'')
if excludeAmbiguousChar:
    for AChar in AmbiguousChar:
        stringsCollect = stringsCollect.replace(AChar,'')
        
        
stringsDB = "".join(stringsCollect)


# save random password in list
passwordStringsList = []

while len(passwordStringsList) <= numberChar:
    generateDigit = random.choice(stringsDB)
    passwordStringsList.append(generateDigit)

passwordStrings = "".join(passwordStringsList)
try:
    clip.copy(passwordStrings)
except:
    print(passwordStrings)
print(passwordStrings,'\t [copied]')


 
