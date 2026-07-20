import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Task 4: Plot stopping voltage vs frequency in Hz (or in-vacuum wavelength in nm) of incident photons for various metals.")

fig, ax = plt.subplots()

# define constants
h = 6.626e-34
e = 1.602176620898e-19
freqs = np.linspace(0, 3e15, 10)

workFunctions = {
    "Ag": 4.3,
    "Al": 4.3,
    "Au": 5.1,
    "Cu": 4.7,
    "Sn": 4.4,
    "Pb": 4.3,
    "W": 4.5,
    "Ni": 4.6,
    "Na": 2.4
}

# loop through each material and calculate
for material, workEv in workFunctions.items():
    W = (workEv * e)
    V = ((h/e)*freqs) - (W/e)
    freqCutoff = W/h
    
    # plot everything nicely w/ labels, etc...
    ax.scatter(freqCutoff, 0, s=30)
    ax.plot(freqs, V, label=material)
    ax.set_title("Photoelectric Effect: Multiple metals")
    ax.set_xlabel("Frequency / Hz (x10^15)")
    ax.set_ylabel("Stopping voltage / Volts")
    ax.grid(linestyle = '--')      
    ax.legend()
    
st.pyplot(fig)