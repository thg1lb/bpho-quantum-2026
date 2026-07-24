import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
# classicMatch = (cosSquaredTheta*cosSquaredPhi) + (sinSquaredTheta*sinSquaredPhi)
classicMismatch = (1 - (cosSquaredTheta*cosSquaredPhi) - (sinSquaredTheta*sinSquaredPhi))

# quantum probabilities
phiThetaSubtraction = phiRadians - thetaRadians
# quantumMatch = (np.cos(phiThetaSubtraction))**2
quantumMismatch = (np.sin(phiThetaSubtraction))**2

st.write("Classical Mismatch = ")
st.write(f"{classicMismatch:.2%}")
st.write("Quantum Mismatch = ")
st.write(f"{quantumMismatch:.2%}")