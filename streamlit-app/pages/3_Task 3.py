import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Task 3: Plot the Planck spectrum B(lamda,T) and Einstein’s model of the heat capacity C of solids.



# constant definitions
kb = 1.381e-23
h = 6.626e-34
c = 2.998e8
R = 8.314  

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()


def planckSpectrum():
        
        temps = np.array([4000, 5000, 6000])
        wavelengths = np.linspace(100e-9, 2500e-9, 100)
        
        # loop through each temp and calculate intensity
        for T in temps:
            
            # formulae from BPho CompPhys slides
            exponentThing = (h*c)/(wavelengths*kb*T)
            B = ((2*h*(c**2))/wavelengths**5)*(1/(np.exp(exponentThing) - 1))
            
            ax1.plot(wavelengths*1e9, B, label=f"T = {T} K")  
            ax1.set_xlabel("Wavelength / nm")
            ax1.set_ylabel("Irradiance / Wm^-2 / nm")
            ax1.legend() 
    
def einsteinModel():
     
    temps = np.linspace(10, 800, 800)
     
    einsteinFreqs = {
        "Au": 0.2855e13,
        "Cu": 0.5769e13,
        "Ti": 0.7054e13,
        "Al": 0.7188e13,
        "Fe": 0.7893e13,
        "Si": 1.0832e13,
        "C": 3.7451e13
    }
    
    # loop through materials and calculate 
    for material, f_E in einsteinFreqs.items():
        
        # formulae from BPho CompPhys slides 
        x = ((h)*f_E)/(kb*temps)
        C = ((3*R)*(x**2)*(np.exp(x)))/((np.exp(x) - 1)**2)
        
        ax2.plot(temps, C, label=material)
        ax2.set_xlabel("Temperature / K")
        ax2.set_ylabel("Heat capacity / J mol$^{-1}$ K$^{-1}$")
        ax2.legend()
    
planckSpectrum()
st.subheader("Planck Spectrum at Different Temperatures")

st.caption(
    "Increasing the black-body temperature increases the spectral radiance "
    "and shifts the peak towards shorter wavelengths."
)
st.pyplot(fig1)


einsteinModel()  
st.subheader("Einstein Model of Heat Capacity")

st.caption(
    "As temperature increases, the heat capacities approach the classical "
    "Dulong-Petit limit of 3R. Different Einstein frequencies determine how "
    "quickly each material approaches this limit."
)

st.pyplot(fig2)

