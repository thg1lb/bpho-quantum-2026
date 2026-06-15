import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np

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
    
    plt.figure(1)
    plt.plot(thetaDegrees, fractionalShift, label=f"E={energy}keV")
    plt.title("Compton Scattering of X-ray photon off an electron")
    plt.xlabel("Photon Scattering angle theta / degrees")
    plt.ylabel("fractional shift")
    plt.legend()
    
    # recoil speed (calculations + plotting)
    electronRestEnergy = massE*(c**2)
    lambdaFinal = deltaLambda + lambdaInitial
    initialEnergy = (h*c)/lambdaInitial
    finalEnergy = (h*c)/lambdaFinal
    
    v = c*(np.sqrt((1-((electronRestEnergy)/(initialEnergy - finalEnergy + electronRestEnergy)))**2))
    vOverc = v/c
    
    plt.figure(2)
    plt.plot(thetaDegrees, vOverc, label=f"E={energy}keV")
    plt.title("Compton Scattering of X-ray photon off an electron")
    plt.xlabel("Photon Scattering angle theta / degrees")
    plt.ylabel("Electron recoil speed v/c")
    plt.legend()
    
    # recoil angle (calculations + plotting)
    sinTheta = np.sin(theta)
    cosTheta = np.cos(theta)
    photonEnergyRatio = h/(massE*c*lambdaInitial)
    denominator = 1 + (photonEnergyRatio * (1 - cosTheta)) - cosTheta
    phi = np.arctan2(sinTheta, denominator)
    
    plt.figure(3)
    plt.plot(thetaDegrees, np.degrees(phi), label=f"E={energy}keV")
    plt.title("Compton Scattering of X-ray photon off an electron")
    plt.xlabel("Photon Scattering angle theta / degrees")
    plt.ylabel("Electron recoil angle phi / degrees")
    plt.legend()
    
plt.show()