import itertools
from util import save
import threading

class myThread(threading.Thread):

    def __init__(self, passLen, chars, outputFile):
        threading.Thread.__init__(self)
        self.passLen = passLen
        self.chars = chars
        self.outputFile = outputFile

    def run(self):
        # Counter for 99999 to save generated password in output file
        i = 0

        # Generate password list by itertools
        passwords = itertools.product(self.chars, repeat=self.passLen)

        outputList = []
        for password in passwords:

            # Check counter to save generated passwords into the output file
            if i == 99999:
                save(tup=outputList, outFile=self.outputFile)
                i = 0

                # Clear list to avoid of memory leak
                outputList.clear()
            
            # Convert tuple to string
            it = ''.join(password)

            print(it)
            i += 1

            # Append the generated password to list
            outputList.append(it)

        # Saving the last items that are in memory (RAM) and they are not stored in before
        save(outputList, self.outputFile)
