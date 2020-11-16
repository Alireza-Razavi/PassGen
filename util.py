import re

# The save function to storing passwords to a file
def save(tup, outFile):
     tl = list(tup)
     tl = '\n'.join(tl)
     tl += '\n'
     outFile.write(tl)

def isRangeOK(data):
     x = re.findall('([0-9]?)\d-[0-9](\d?)', data)
     return len(x) == 1