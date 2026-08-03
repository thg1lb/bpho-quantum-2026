import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
from math import factorial

# constants
e0 = 8.8418782e-12
e = 1.602176620898e-19
h = 6.626e-34
mE = 9.1094e-31

# test values using Carbon-12 from slides
r = np.linspace(0, 4, 1000) # radius in angstroms
Z = 6 # proton number
A = 12 # atomic mass in u
n = 4 # principal quantum number
L = 2 # angular momentum quantum number
a0 = (e0*(h**2))/(np.pi*(mE*(np.exp(2))))
M = 12 # for now since nucleus mass of c-12 is roughly 12u
mu = (mE*M)/(mE + M)
a = (4*np.pi*e0*(h**2))/(mu*np.exp(2))
x = (2*r)/(a*n)



laguerre = 0

for k in range (0, (n-L)):
    laguerre += (((factorial(L+n))*((-x)**k))/((factorial((2*L)+1+k))*(factorial(n-L-1-k))*(factorial(k))))

radial = np.sqrt((factorial(n-L-1))/(2*n*(factorial(n+L))))*((2*(a*n))**(3/2))*(x**L)*(np.exp(-x/2)) * laguerre

probabilityDensity = (np.abs(radial))**2

plt.plot(r, probabilityDensity)
plt.xlabel("radius / angstroms")
plt.ylabel("probability density")
plt.show()