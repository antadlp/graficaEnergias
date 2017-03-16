import matplotlib.pyplot as plt
import numpy as np

def fftFunction01(x):

   fx = []
   N = len(x)
   for k in range(N):
      for n in range(N):
         fx.append(x[k]*\
               np.cos(2*np.pi*(k-1)*(n-1)/N) + \
               np.sin(2*np.pi*(k-1)*(n-1)/N)j)

    return fx;




x = linspace(1, 10, 10)
fftx = fftFunction01(x)

print(fftx)

   
   
   



