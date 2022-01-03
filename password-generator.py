import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


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

# preparation stringsDB depend on params
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


# save random password in a list
passwordStringsList = []

while len(passwordStringsList) <= numberChar:
    generateDigit = random.choice(stringsDB)
    passwordStringsList.append(generateDigit)
# join the passwordStringsList
passwordStrings = "".join(passwordStringsList)

# auto copy features
if autoCopy:
    import pyperclip as clip
    clip.copy(passwordStrings)
    print(passwordStrings,'\t [copied]')
else:
    print(passwordStrings)
 
