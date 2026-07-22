import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Task 5: a graph of photon energy vs wavelength for photon emissions from hydrogen atoms due to transitions between electron energy levels.")

# constant definitions
e0 = 8.8418782e-12
e = 1.602176620898e-19
h = 6.626e-34
c = 2.998e8
massE = 9.1093837e-31

fig, ax = plt.subplots()

spectralLines = {
    
    "Lyman": 1,
    "Balmer": 2,
    "Paschen": 3,
    "Brackett": 4,
    "Pfund": 5
     
}

# loop through dictionary
for spectralLine, m in spectralLines.items():
    
    # arrays to store values needed for plotting
    wavelengthsNm = []
    energiesEv = []
    
    # loop through emission transitions from n to m
    # where m is the fixed lower level and n is the variable upper level
    for n in range (m+1, 15):
    
    # formulae from BPho CompPhys slides
     wavelength = ((8*(e0**2)*(h**3)*c)/(massE*(e**4)))*(((1/(m**2))-(1/(n**2)))**-1)
     wavelengthInNm = wavelength * 1e9
     
     energy = ((h*c)/wavelength) / e
     
     # append calculated values to arrays (allows us to plot all values at once)
     wavelengthsNm.append(wavelengthInNm)
     energiesEv.append(energy)
     
    # plotting (+ labels, etc...)
    ax.scatter(wavelengthsNm, energiesEv, label=spectralLine, linestyle="--")
    ax.set_title("Bohr model of Hydrogenic atom photon emissions: Z = 1")
    ax.set_xlabel("wavelength (nm)")
    ax.set_ylabel("Photon energy (eV)")
    ax.legend() 
     
st.pyplot(fig)
    