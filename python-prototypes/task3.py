<<<<<<< HEAD
import matplotlib.pyplot as plt, numpy as np
from scipy.integrate import quad

def planckSpectrum():
    
        # constant definitions
        kb = 1.381e-23
        global h 
        h = 6.626e-34
        c = 2.998e8
        
        temps = np.array([4000, 5000, 6000])
        wavelengths = np.linspace(100e-9, 2500e-9, 100)
        
        # equations
        # sigma = ((2*(np.pi)**5)(kb**4))/(15(c**2)(h**3))
        for T in temps:
            
            exponentThing = (h*c)/(wavelengths*kb*T)
            B = ((2*h*(c**2))/wavelengths**5)*(1/(np.exp(exponentThing) - 1))
            plt.plot(wavelengths*1e9, B, label=f"T = {T} K")  
            plt.xlabel("Wavelength / nm")
            plt.ylabel("Irradiance / Wm^-2 / nm")
            plt.legend() 
        
    
    
def einsteinModel():
    
    R = 8.314  
     
    temps = np.linspace(0, 800, 800)
     
    einsteinFreqs = {
        "Au": 0.2855e13,
        "Cu": 0.5769e13,
        "Ti": 0.7054e13,
        "Al": 0.7188e13,
        "Fe": 0.7893e13,
        "Si": 1.0832e13,
        "C": 3.7451e13
    }
        
plt.show()
    
planckSpectrum()
    

        
    
    
    
    
=======
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
        
        # equations
        # sigma = ((2*(np.pi)**5)(kb**4))/(15(c**2)(h**3))
        for T in temps:
            
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
    
    for material, f_E in einsteinFreqs.items():
        x = ((h)*f_E)/(kb*temps)
        C = ((3*R)*(x**2)*(np.exp(x)))/((np.exp(x) - 1)**2)
        
        plt.plot(temps, C, label=material)
    
plt.figure()
planckSpectrum()

plt.figure()
einsteinModel()

plt.show()
>>>>>>> c123734fefc9040288e303039c7ae02029bd24ff
