import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Task 7: energy vs quantum number n, and probability densities vs x, for wavefunctions for a ‘particle in a box.’

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

e = 1.602176620898e-19
m = 9.1094e-31
h = 6.626e-34
a = 0.529e-10 # roughly from graph (Bohr radius)
hbar = h/(2*np.pi)
n = np.array([1, 2, 3])   
x = np.linspace(0, a, 1000)

energies  = []

def energyVsQuantum():
    # calculations
    for value in n:
        E_n = ((hbar**2)*((np.pi)**2)*(value**2)) / (2*m*(a**2))
        energies.append(E_n)
        
    energiesInEv = np.array(energies) / e
    ax1.scatter(n, energiesInEv)
    ax1.set_xlim(0, 3)
    ax1.set_ylim(0, None)
        
    st.subheader("Particle in a Box: Quantised Energy Levels")

    st.caption(
        "Only discrete energy levels are permitted inside the infinite potential well, "
        "with energy increasing as the square of the quantum number n."
    )    
    st.pyplot(fig1)
    
def probabilityVsX():
    
    for value in n:
        psi = np.sqrt(2/a) * np.sin(value*(np.pi)*(x/a))
        probDensity =  psi**2
        xAngstroms = x * 1e10
        
        ax2.plot(xAngstroms, probDensity)
        ax2.set_xlabel("x / angstroms")
        ax2.set_ylabel("Probability density")
    
    st.subheader("Particle in a Box: Probability Density")

    st.caption(
        "The probability density |ψ|² describes where the confined particle is most "
        "likely to be detected, with zero probability at the walls of the box."
    )
    st.pyplot(fig2)
    
probabilityVsX()
energyVsQuantum()