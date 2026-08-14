import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from math import factorial
from scipy.special import sph_harm_y
import streamlit as st

# Challenge #10: Hydrogenic orbitals. Use the mathematical recipe (see the next few
# slides) for the wavefunctions of a Hydrogenic atom (i.e. one electron, Z protons) to
# plot maps of probability density, given quantum numbers n, l, m.

st.subheader("3D Hydrogenic Orbital Probability Density")

st.caption(
    "The hydrogenic wavefunction is evaluated throughout three-dimensional space. "
    "Only points above the selected relative probability-density threshold are "
    "displayed to make the orbital structure visible."
)

# constants
e0 = 8.8418782e-12 # permittivity of free space
e = 1.602176620898e-19 
h = 6.626e-34
mE = 9.1094e-31
u = 1.66053906660e-27

# user selected atom/quantum numbers
Z = st.sidebar.slider("Proton number Z", 1, 10, 6)
A = st.sidebar.slider("Mass number A", Z, 20, 12)
n = st.sidebar.slider("Principal quantum number n", 1, 6, 4)

# n = 1 only works if l = 0
if n == 1:
    L = 0
    st.write("angular momentum quantum number L = 0")
else:
    L = st.sidebar.slider(
        "Angular momentum quantum number L", 0, n - 1, min(2, n - 1))

# l = 0 only works if m = 0
if L == 0:
    m = 0
    st.write("magnetic quant num m = 0")

else:
    m = st.sidebar.slider("Magnetic quantum number m", -L, L, 0)

# coord ranges for the sph. harmonics
theta = np.linspace(0, np.pi, 200) 
phi = np.linspace(0, 2*np.pi, 200)

def radial(rValues):
    # calculates the bohr radius and converts from meters to angstroms
    a0 = (e0*(h**2))/(np.pi*(mE*e**2))
    a0 = a0/1e-10
    
    # approx nuclear mass
    M = A * u # nucleus mass in kg
    mu = (mE*M)/(mE + M) # calculation for reduced mass
    
    # radii calculations
    a = (mE*a0)/(mu*Z) 
    x = (2*rValues)/(a*n)

    # laguerre-polynomial summation
    laguerre = 0

    for k in range (0, (n-L)):
        laguerre += (((factorial(L+n))*((-x)**k))/((factorial((2*L)+1+k))*(factorial(n-L-1-k))*(factorial(k))))

    # combines all terms
    radial = np.sqrt((factorial(n-L-1))/(2*n*(factorial(n+L))))*((2/(a*n))**(3/2))*(x**L)*(np.exp(-x/2)) * laguerre

    return radial


def spherical(thetaValues, phiValues):
    
    # mapped piecewise definition from task
    if m < 0:
        return(sph_harm_y(L, abs(m), thetaValues, phiValues) - (sph_harm_y(L, -abs(m), thetaValues, phiValues)))
    
    elif m ==0:
        return sph_harm_y(L, 0, thetaValues, phiValues)
    
    else:
        return(sph_harm_y(L, m, thetaValues, phiValues) + sph_harm_y(L, -m, thetaValues, phiValues))
   
    
# grid
axis = np.linspace(-4, 4, 500)

xGrid, yGrid = np.meshgrid(axis, axis)
zGrid = np.zeros_like(xGrid)

# cartesian to sph. coords
rGrid = np.sqrt(xGrid**2 + yGrid**2 + zGrid**2)

thetaGrid = np.arccos(np.divide(zGrid, rGrid, out=np.zeros_like(rGrid), where=rGrid != 0))

phiGrid = np.mod(np.arctan2(yGrid, xGrid), 2*np.pi)

# radial + angular components for wavefunction
R = radial(rGrid)
Y = spherical(thetaGrid, phiGrid)

psi = R * Y

# born int.
probDensity = np.abs(psi)**2

# normalisation
maxDensity = np.max(probDensity)

if maxDensity > 0:
    probDensity /= maxDensity

# plotting
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

# 3d cartesian grid into sph. coords
r3D = np.sqrt(x3D**2 + y3D**2 + z3D**2)

theta3D = np.arccos(np.divide(z3D, r3D, out=np.zeros_like(r3D), where=r3D != 0)) 

phi3D = np.mod(np.arctan2(y3D, x3D), 2*np.pi)

# 3D wavefunction calculation
R3D = radial(r3D)
Y3D = spherical(theta3D, phi3D)

psi3D = R3D * Y3D

# converts wavefunction to prob. dens.
prob3D = np.abs(psi3D)**2

# normalisation relative to maxdens.
max3D = np.max(prob3D)

if max3D > 0:
    prob3D /= max3D
    
# only displays points whose relative dens. is bigger than chosen frac.
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