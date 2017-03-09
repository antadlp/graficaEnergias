import re
import sys


def leeEimprimeZZ(inputFile, outputFile):
   
   F = open(inputFile,'r')
   fileOut = open(outputFile, "w")

   for line in F:
     if re.search(r'\spotential energy\s',line,re.M|re.I):
         fileOut.write(line.split()[2])
         fileOut.write("\n")

   fileOut.close()
   F.close()
   return;


#for line in F:
#  if re.search(r'\spotential energy\s',line,re.M|re.I):
#      #print line
#      #sys.stdout.write(line.split()[2])
#      print line.split()[2]
#
#

      
leeEimprimeZZ('zz', "ver3.dat")
leeEimprimeZZ('zz', "ver4.dat")



