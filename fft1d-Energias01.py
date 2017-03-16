import re
import sys
from buscaEimprime001 import leeEpasaArregloDAT
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack





# get the values of energy from .dat files which has been
# obtained from ./buscaEimprime001.py 

eGP = leeEpasaArregloDAT('../datosMallaPython/eGP.dat')
eBN = leeEpasaArregloDAT('../datosMallaPython/eBN.dat')
eB23N23 = leeEpasaArregloDAT('../datosMallaPython/eB23N23.dat')
eB2N2 = leeEpasaArregloDAT('../datosMallaPython/eB2N2.dat')
eB3N3 = leeEpasaArregloDAT('../datosMallaPython/eB3N3.dat')
eB6N6 = leeEpasaArregloDAT('../datosMallaPython/eB6N6.dat')
eB12N12a = leeEpasaArregloDAT('../datosMallaPython/eB12N12a.dat')
eB12N12b = leeEpasaArregloDAT('../datosMallaPython/eB12N12b.dat')
eB12N12c = leeEpasaArregloDAT('../datosMallaPython/eB12N12c.dat')
eB12N12d = leeEpasaArregloDAT('../datosMallaPython/eB12N12d.dat')
eB12N12e = leeEpasaArregloDAT('../datosMallaPython/eB12N12e.dat')


# define x-axis array representing time

x = np.linspace(1.0, 5000, 5000)


# compute fft 1-dimensional 

eGPFFTdot = np.multiply(scipy.fftpack.fft(eGP), \
      np.conjugate(scipy.fftpack.fft(eGP)))

print("\n")
print('el max eGPFFTdot es %f ') % np.max(eGPFFTdot)
print("\n")
print(np.where(eGPFFTdot==eGPFFTdot.max()))
print("\n")

# plot time vs energy

fig = plt.figure(0)        
fig.canvas.set_window_title('time vs Energy GP')
plt.plot(x, eGP, color='blue', linewidth=1.0, linestyle='-')

# plot time vs fft-energy

fig = plt.figure(1)        
fig.canvas.set_window_title('time vs Energy FFT GP')
plt.plot(x, eGPFFTdot, color='blue', linewidth=1.0, linestyle='-')






plt.show()

# plot time vs fft-energy

## UTILITIES ## Templates for possible functions to use
#
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.plot(x, eGP, 'r--')











