import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from math import factorial
from scipy.special import sph_harm_y
import streamlit as st

# constants
e0 = 8.8418782e-12
e = 1.602176620898e-19
h = 6.626e-34
mE = 9.1094e-31
u = 1.66053906660e-27

# # test values using Carbon-12 from slides
# r = np.linspace(0, 4, 1000) # radius in angstroms
# Z = 6 # proton number
# A = 12 # atomic mass in u
# n = 4 # principal quantum number
# L = 2 # angular momentum quantum number
# m = 0 # magnetic quantum number

Z = st.slider("Proton number Z", 1, 10, 6)
A = st.slider("Mass number A", Z, 20, 12)

n = st.slider("Principal quantum number n", 1, 6, 4)

if n == 1:
    L = 0
    st.write("angular momentum quantum number L = 0")
else:
    L = st.slider(
        "Angular momentum quantum number L", 0, n - 1, min(2, n - 1))

# minor error handling
if L == 0:
    m = 0
    st.write("magnetic quant num m = 0")

else:
    m = st.slider("Magnetic quantum number m", -L, L, 0)

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
    
    if m < 0:
        return(sph_harm_y(L, abs(m), thetaValues, phiValues) - (sph_harm_y(L, -abs(m), thetaValues, phiValues)))
    
    elif m ==0:
        return sph_harm_y(L, 0, thetaValues, phiValues)
    
    else:
        return(sph_harm_y(L, m, thetaValues, phiValues) + sph_harm_y(L, -m, thetaValues, phiValues))
   
    

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

maxDensity = np.max(probDensity)

if maxDensity > 0:
    probDensity /= maxDensity

fig, ax = plt.subplots()

mesh = ax.pcolormesh(xGrid, yGrid, probDensity, shading="auto")

ax.set_aspect("equal")
ax.set_xlabel("x / angstroms")
ax.set_ylabel("y / angstroms")
ax.set_title("z = .... etc")

fig.colorbar(mesh, ax=ax)

st.pyplot(fig)