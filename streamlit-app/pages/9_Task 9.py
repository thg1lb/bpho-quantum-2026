import streamlit as st
import matplotlib.pyplot as plt, numpy as np

st.title("Task 9: Compton Scattering. Plot fractional wavelength shift , election recoil speed v and electron recoil angle  vs photon scattering angle .")

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()


# constant definitions
e = 1.602176620898e-19
h = 6.626e-34
c = 2.998e8
massE = 9.1093837e-31

# values taken from slide
energiesKev = [50, 100, 200, 500, 1000]


# defining an angle (theta) to be used for each graph
thetaDegrees = np.linspace(0, 180, 1000)
theta = np.radians(thetaDegrees)


for energy in energiesKev:
    
    # fractional shift (calculations + plotting)
    energyJ = energy * 1000 * e
    lambdaInitial = (h*c)/energyJ
    deltaLambda = (h/(massE*c))*(1 - np.cos(theta))
    
    fractionalShift = deltaLambda/lambdaInitial
    
    ax1.plot(thetaDegrees, fractionalShift, label=f"E={energy}keV")
    ax1.set_title("Compton Scattering of X-ray photon off an electron")
    ax1.set_xlabel("Photon Scattering angle theta / degrees")
    ax1.set_ylabel("fractional shift")
    ax1.legend()
    
    # recoil speed (calculations + plotting)
    electronRestEnergy = massE*(c**2)
    lambdaFinal = deltaLambda + lambdaInitial
    initialEnergy = (h*c)/lambdaInitial
    finalEnergy = (h*c)/lambdaFinal
    
    v = c*(np.sqrt((1-((electronRestEnergy)/(initialEnergy - finalEnergy + electronRestEnergy)))**2))
    vOverc = v/c
    
    ax2.plot(thetaDegrees, vOverc, label=f"E={energy}keV")
    ax2.set_title("Compton Scattering of X-ray photon off an electron")
    ax2.set_xlabel("Photon Scattering angle theta / degrees")
    ax2.set_ylabel("Electron recoil speed v/c")
    ax2.legend()
    
    # recoil angle (calculations + plotting)
    sinTheta = np.sin(theta)
    cosTheta = np.cos(theta)
    photonEnergyRatio = h/(massE*c*lambdaInitial)
    denominator = 1 + (photonEnergyRatio * (1 - cosTheta)) - cosTheta
    phi = np.arctan2(sinTheta, denominator)
    
    ax3.plot(thetaDegrees, np.degrees(phi), label=f"E={energy}keV")
    ax3.set_title("Compton Scattering of X-ray photon off an electron")
    ax3.set_xlabel("Photon Scattering angle theta / degrees")
    ax3.set_ylabel("Electron recoil angle phi / degrees")
    ax3.legend()
    
st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)