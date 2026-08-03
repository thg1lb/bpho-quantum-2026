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
u = 1.66053906660e-27

# test values using Carbon-12 from slides
r = np.linspace(0, 4, 1000) # radius in angstroms
Z = 6 # proton number
A = 12 # atomic mass in u
n = 4 # principal quantum number
L = 2 # angular momentum quantum number

def radial():
    
    a0 = (e0*(h**2))/(np.pi*(mE*e**2))
    a0 = a0/1e-10

    M = A * u # nucleus mass in kg
    mu = (mE*M)/(mE + M)
    a = (mE*a0)/(mu*Z)
    x = (2*r)/(a*n)

    laguerre = 0

    for k in range (0, (n-L)):
        laguerre += (((factorial(L+n))*((-x)**k))/((factorial((2*L)+1+k))*(factorial(n-L-1-k))*(factorial(k))))

    radial = np.sqrt((factorial(n-L-1))/(2*n*(factorial(n+L))))*((2/(a*n))**(3/2))*(x**L)*(np.exp(-x/2)) * laguerre

    probabilityDensity = (np.abs(radial))**2

    plt.plot(r, probabilityDensity)
    plt.xlabel("radius / angstroms")
    plt.ylabel("probability density")
    plt.show()
    
radial()