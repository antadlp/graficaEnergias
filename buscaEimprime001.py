import re
import sys

with open('zz','r') as searchfile:
    for line in searchfile:
        if re.search(r'\spotential energy\s',line,re.M|re.I):
            #print line
            sys.stdout.write(line)


