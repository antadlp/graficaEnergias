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



def saveArrayToFile(array, outputFile):
 
   fileOut = open(outputFile, "w")

   for p in array[50:(len(array)-1)]:
      fileOut.write(str(p))
      fileOut.write("\n")

   
   fileOut.close()
   return;


eGP = leeEpasaArregloZZ('../datosMallaPython/zz-GP.dat')
eBN = leeEpasaArregloZZ('../datosMallaPython/zz-BN.dat')
eBN23N23 = leeEpasaArregloZZ('../datosMallaPython/zz-B23N23.dat')
eB2N2 = leeEpasaArregloZZ('../datosMallaPython/zz-B2N2.dat')
eB3N3 = leeEpasaArregloZZ('../datosMallaPython/zz-B3N3.dat')
eB6N6 = leeEpasaArregloZZ('../datosMallaPython/zz-B6N6.dat')
eB12N12a = leeEpasaArregloZZ('../datosMallaPython/zz-B12N12a.dat')
eB12N12b = leeEpasaArregloZZ('../datosMallaPython/zz-B12N12b.dat')
eB12N12c = leeEpasaArregloZZ('../datosMallaPython/zz-B12N12c.dat')
eB12N12d = leeEpasaArregloZZ('../datosMallaPython/zz-B12N12d.dat')
eB12N12e = leeEpasaArregloZZ('../datosMallaPython/zz-B12N12e.dat')


saveArrayToFile(eGP, '../datosMallaPython/eGP.dat')
saveArrayToFile(eBN, '../datosMallaPython/eBN.dat')
saveArrayToFile(eBN23N23, '../datosMallaPython/eBN23N23.dat')
saveArrayToFile(eB2N2, '../datosMallaPython/eB2N2.dat')
saveArrayToFile(eB3N3, '../datosMallaPython/eB3N3.dat')
saveArrayToFile(eB6N6, '../datosMallaPython/eB6N6.dat')
saveArrayToFile(eB12N12a, '../datosMallaPython/eB12N12a.dat')
saveArrayToFile(eB12N12b, '../datosMallaPython/eB12N12b.dat')
saveArrayToFile(eB12N12c, '../datosMallaPython/eB12N12c.dat')
saveArrayToFile(eB12N12d, '../datosMallaPython/eB12N12d.dat')
saveArrayToFile(eB12N12e, '../datosMallaPython/eB12N12e.dat')
   


