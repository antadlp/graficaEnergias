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

def leeEpasaArregloZZ(inputFile):
   
   F = open(inputFile,'r')

   A = []
   for line in F:
      if re.search(r'\spotential energy\s',line,re.M|re.I):
         A.append(float(line.split()[2]))


   F.close()
   return A;

#leeEimprimeZZ('zz', "ver3.dat")
#leeEimprimeZZ('zz', "ver4.dat")

B = leeEpasaArregloZZ('zz')

for p in B[0:10]:
   print(p)


   


