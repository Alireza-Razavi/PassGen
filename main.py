import sys
from util import isRangeOK
from myThread import myThread

args = sys.argv

# Check required parameters is passed
if len(args) != 4:
    print('############################################################')
    print("Usage:\n\t- python main.py <string> <output> <length>")
    print('\t- example: python main.py abcdefgh output.txt 8-12')
    print('############################################################')
    exit(1)

# Parsing passed parameters into local variables     
characters = args[1]
outputFileName = args[2]
passwordLength = args[3]

# Check the regex
if not isRangeOK(passwordLength):
    print('Invalid <length> format!\n<length> must be in this format: xx-yy')
    exit(1)

# Divide the range into two variables
startRange = int(passwordLength.split("-")[0])
endRange = int(passwordLength.split("-")[1])

# The static characters for all password lists
staticChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '@', '+', '-', '?', '.', '_']

# Split the passed string character by character 
chars = []
for ch in characters:
    # Check for lower case characters
    if ch.isupper():
        print("Error -> You must enter the string in lower case!")
        exit(1)
    
    # Check for pre-defined program characters
    if ch in staticChars:
        print("Error -> The char '" + ch +  "' has defined in pre-defined program characters!")
        exit(1)

    # Check for duplicate characters
    j = 0
    for c in characters:
        if c == ch:
            j += 1
    if j > 1:
        print("Error -> '" + characters + "' has duplicate characters!")
        exit(1)
        
    chars.append(ch)

# Add upper case characters to list
upChars = characters.upper()
for ch in upChars:
    chars.append(ch)

# Concat two lists into a single list
chars = chars + staticChars

# Starting the threads
for i in range(startRange, endRange + 1):
    fileName = 'output/' + outputFileName.split(".")[0] + "-" + str(i) + "." + outputFileName.split(".")[1]
    mFile = open(fileName, 'w')
    mFile.write('')
    mFile = open(fileName, 'a')

    th = myThread(i, chars, mFile)
    th.start()