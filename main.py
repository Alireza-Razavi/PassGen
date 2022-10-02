import sys
from util import isRangeOK
from myThread import myThread

def listToString(mList):
    forbiddenSigns = ['|', '<', '>', '?', '"', '*', '/', "\\", ':']
    outStr = ""
    for x in mList:
        if x not in forbiddenSigns:
            outStr += x
    return outStr

args = sys.argv

# Check required parameters is passed
if len(args) != 3:
    print('############################################################')
    print("Usage:\n\t- python main.py <string> <range>")
    print('\t- example: python main.py abcdefgh 8-12')
    print('############################################################')
    exit(1)

# Parsing passed parameters into local variables     
characters = args[1]
passwordLength = args[2]

# Check the regex
if not isRangeOK(passwordLength):
    print('Invalid <length> format!\n<length> must be in this format: xx-yy')
    exit(1)

# Divide the range into two variables
startRange = int(passwordLength.split("-")[0])
endRange = int(passwordLength.split("-")[1])

# The constant characters for all password lists
constChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '+', '-', '?', '.', '_']

# Split the passed string character by character 
chars = []
for ch in characters:
    # Check for lower case characters
    if ch.isupper():
        print("Error -> Please enter all input characters in lower case!")
        exit(1)
    
    # Check for pre-defined program characters
    if ch in constChars:
        continue

    # Check for duplicate characters
    j = 0
    for c in characters:
        if c == ch:
            j += 1
    if j > 1:
        continue
  
    chars.append(ch)

    if ch.isalpha() == True:
        chars.append(ch.upper())

# Concat two lists into a single list
chars = chars + constChars

# Starting the threads
for i in range(startRange, (endRange + 1)):
    fileName = 'output/input=' + listToString(chars) + "____len=" + str(i) + ".txt"
    mFile = open(fileName, 'w')
    mFile.write('')
    mFile = open(fileName, 'a')

    th = myThread(i, chars, mFile)
    th.start()
