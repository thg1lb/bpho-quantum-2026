import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

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
    
    ax.plot(voltages/1000, x*1000, label=label)
    ax.set_title("Rings of radius x vs accelerating voltage")
    ax.set_xlabel("Voltage / kV")
    ax.set_ylabel("Ring radius / mm")
    ax.legend() 

st.pyplot(fig)