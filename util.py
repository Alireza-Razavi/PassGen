<<<<<<< HEAD
import re

# The save function to storing passwords to a file
def save(tup, outFile):
     tl = list(tup)
     tl = '\n'.join(tl)
     tl += '\n'
     outFile.write(tl)

def isRangeOK(data):
     x = re.findall('([0-9]?)\d-[0-9](\d?)', data)
=======
import re

# The save function to storing passwords to a file
def save(tup, outFile):
     tl = list(tup)
     tl = '\n'.join(tl)
     tl += '\n'
     outFile.write(tl)

def isRangeOK(data):
     x = re.findall('([0-9]?)\d-[0-9](\d?)', data)
>>>>>>> 1b630ed91d1f6bc3df3471bb7b73d7c15e50ed21
     return len(x) == 1