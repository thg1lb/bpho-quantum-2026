import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Task 6: a computer model of the rings (of radius x) on the phosphor screen vs accelerating voltage V. Take r = 65mm and d = 0.123 nm or 0.213 nm. Range of V is 1 to 5 kV

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# constant definitions
e = 1.602176620898e-19
h = 6.626e-34
c = 2.998e8
massE = 9.1093837e-31

r = 65e-3

dValues = {
    
    "0.123 nm": 0.123e-9,
    "0.213 nm": 0.213e-9 
    
}

voltages = np.linspace(1000, 5000, 100)

# loop through d values
for label, d in dValues.items():
    
    # calculations
    wavelengths = h/np.sqrt(2*massE * e * voltages)
    phi = np.arcsin(wavelengths/(2*d))
    x = r * np.sin(2*phi)
    
    ax1.plot(voltages/1000, x*1000, label=label)
    ax1.set_title("Rings of radius x vs accelerating voltage")
    ax1.set_xlabel("Voltage / kV")
    ax1.set_ylabel("Ring radius / mm")
    ax1.legend() 
    
    # checker graph
    xCheck = 1/np.sqrt(voltages)
    yCheck = np.sin(phi)
    ax2.scatter(xCheck, yCheck, label=label)
    ax2.set_title("Ring Radius vs 1/sqrt(accelerating voltage)")

st.subheader("Electron Diffraction Ring Radius vs Accelerating Voltage")

st.caption(
    "The diffraction ring radius decreases as the accelerating voltage increases. "
    "The two curves correspond to the two graphite lattice spacings."
)
st.pyplot(fig1)

st.subheader("Linearised Electron Diffraction Relationship")

st.caption(
    "Plotting ring radius against 1/√V gives an approximately linear relationship, "
    "confirming the predicted dependence of ring radius on accelerating voltage."
)
st.pyplot(fig2)