import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
from math import factorial
from scipy.special import sph_harm_y

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
m = 0 # magnetic quantum number

theta = np.linspace(0, np.pi, 200) 
phi = np.linspace(0, 2*np.pi, 200)

def radial(rValues):
    
    a0 = (e0*(h**2))/(np.pi*(mE*e**2))
    a0 = a0/1e-10
    
    M = A * u # nucleus mass in kg
    mu = (mE*M)/(mE + M)
    a = (mE*a0)/(mu*Z)
    x = (2*rValues)/(a*n)

    laguerre = 0

    for k in range (0, (n-L)):
        laguerre += (((factorial(L+n))*((-x)**k))/((factorial((2*L)+1+k))*(factorial(n-L-1-k))*(factorial(k))))

    radial = np.sqrt((factorial(n-L-1))/(2*n*(factorial(n+L))))*((2/(a*n))**(3/2))*(x**L)*(np.exp(-x/2)) * laguerre

    return radial


def spherical(thetaValues, phiValues):
    return sph_harm_y(L, m, thetaValues, phiValues)

axis = np.linspace(-4, 4, 500)

xGrid, yGrid = np.meshgrid(axis, axis)
zGrid = np.zeros_like(xGrid)

rGrid = np.sqrt(xGrid**2 + yGrid**2 + zGrid**2)

thetaGrid = np.arccos(np.divide(zGrid, rGrid, out=np.zeros_like(rGrid), where=rGrid != 0))

phiGrid = np.mod(np.arctan2(yGrid, xGrid), 2*np.pi)

R = radial(rGrid)
Y = spherical(thetaGrid, phiGrid)

psi = R * Y
probDensity = np.abs(psi)**2
probDensity /= np.max(probDensity)

fig, ax = plt.subplots()

mesh = ax.pcolormesh(xGrid, yGrid, probDensity, shading="auto")

ax.set_aspect("equal")
ax.set_xlabel("x / angstroms")
ax.set_ylabel("y / angstroms")
ax.set_title("z = .... etc")

fig.colorbar(mesh, ax=ax)

plt.show()