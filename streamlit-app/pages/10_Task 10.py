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

Z = st.sidebar.slider("Proton number Z", 1, 10, 6)
A = st.sidebar.slider("Mass number A", Z, 20, 12)

n = st.sidebar.slider("Principal quantum number n", 1, 6, 4)

if n == 1:
    L = 0
    st.write("angular momentum quantum number L = 0")
else:
    L = st.sidebar.slider(
        "Angular momentum quantum number L", 0, n - 1, min(2, n - 1))

# minor error handling
if L == 0:
    m = 0
    st.write("magnetic quant num m = 0")

else:
    m = st.sidebar.slider("Magnetic quantum number m", -L, L, 0)

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

# 3D visualisation

axis3D = np.linspace(-1, 4, 60)

x3D, y3D, z3D = np.meshgrid(axis3D, axis3D, axis3D, indexing="ij")

r3D = np.sqrt(x3D**2 + y3D**2 + z3D**2)

theta3D = np.arccos(np.divide(z3D, r3D, out=np.zeros_like(r3D), where=r3D != 0)) 

phi3D = np.mod(np.arctan2(y3D, x3D), 2*np.pi)

# 3D wavefunction

R3D = radial(r3D)
Y3D = spherical(theta3D, phi3D)

psi3D = R3D * Y3D
prob3D = np.abs(psi3D)**2

max3D = np.max(prob3D)

if max3D > 0:
    prob3D /= max3D
    
threshold = st.sidebar.slider("3D probability density threshold", 0.1, 0.9, 0.3, 0.05)
st.sidebar.caption("Only regions with probability density above this fraction of the maximum density are displayed.")
mask = prob3D >= threshold

fig3D = plt.figure()
ax3D = fig3D.add_subplot(111, projection="3d")

scatter = ax3D.scatter(
    x3D[mask],
    y3D[mask],
    z3D[mask],
    c=prob3D[mask],
    s=8,
    alpha=0.6
)

ax3D.set_xlabel("x / angstroms")
ax3D.set_ylabel("y / angstroms")
ax3D.set_zlabel("z / angstroms")
ax3D.set_box_aspect((1, 1, 1))

ax3D.set_title(
    f"3D probability density | n={n}, L={L}, m={m}"
)

fig3D.colorbar(scatter, ax=ax3D)

st.pyplot(fig3D)