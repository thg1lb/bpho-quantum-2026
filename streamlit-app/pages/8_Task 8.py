import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Challenge #8: Create a visual calculator (e.g. some form of GUI or app – although a spreadsheet will suffice) of the Classical and Quantum mismatch probabilities, with the angles theta and phi as variables.")

fig, ax = plt.subplots()

theta = st.slider("theta / degrees", min_value=-90.0, max_value=90.0, value=-30.0, step=1.0)
phi = st.slider("phi / degrees", min_value=-90.0, max_value=90.0, value=30.0, step=1.0)

thetaRadians = np.radians(theta)
phiRadians = np.radians(phi)


# classical probability equation setup
cosSquaredTheta = (np.cos(thetaRadians))**2
cosSquaredPhi = (np.cos(phiRadians))**2

sinSquaredTheta = (np.sin(thetaRadians))**2
sinSquaredPhi = (np.sin(phiRadians))**2

# classical probabilities
classicMatch = (cosSquaredTheta*cosSquaredPhi) + (sinSquaredTheta*sinSquaredPhi)
classicMismatch = (1 - (cosSquaredTheta*cosSquaredPhi) - (sinSquaredTheta*sinSquaredPhi))

# quantum probabilities
phiThetaSubtraction = phiRadians - thetaRadians
quantumMatch = (np.cos(phiThetaSubtraction))**2
quantumMismatch = (np.sin(phiThetaSubtraction))**2

# visuals
dxA = np.cos(thetaRadians) # arrow for detector A using theta
dyB = np.sin(thetaRadians)
ax.arrow(0, 0, dxA, dyB, label="Detector A", color="blue", width=0.01) 

dxC = np.cos(phiRadians) # arrow for detector B using phi
dyD = np.sin(phiRadians)
ax.arrow(0, 0, dxC, dyD, label="Detector B", color="red", width=0.01)

# graphing aesthetic stuff
ax.axis("off")
ax.set_aspect("equal")

ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

ax.set_title("Detector Orientations")
ax.legend()

# output
st.pyplot(fig)
st.write("Classical Mismatch = ")
st.write(f"{classicMismatch:.2%}")
st.write("Quantum Mismatch = ")
st.write(f"{quantumMismatch:.2%}")