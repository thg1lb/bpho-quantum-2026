import matplotlib.pyplot as plt, numpy as np
from scipy.integrate import quad

# constant definitions
kb = 1.381e-23
h = 6.626e-34
c = 2.998e8
R = 8.314  

def planckSpectrum():
        
        temps = np.array([4000, 5000, 6000])
        wavelengths = np.linspace(100e-9, 2500e-9, 100)
        
        # loop through each temp and calculate intensity
        for T in temps:
            
            # formulae from BPho CompPhys slides
            exponentThing = (h*c)/(wavelengths*kb*T)
            B = ((2*h*(c**2))/wavelengths**5)*(1/(np.exp(exponentThing) - 1))
            
            plt.plot(wavelengths*1e9, B, label=f"T = {T} K")  
            plt.xlabel("Wavelength / nm")
            plt.ylabel("Irradiance / Wm^-2 / nm")
            plt.legend() 
        
    
    
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
        
        # formulae from BPho CompPhys slides (may need to fix vars)
        x = ((h)*f_E)/(kb*temps)
        C = ((3*R)*(x**2)*(np.exp(x)))/((np.exp(x) - 1)**2)
        
        plt.plot(temps, C, label=material)
    
plt.figure()
planckSpectrum()

plt.figure()
einsteinModel()

plt.show()
