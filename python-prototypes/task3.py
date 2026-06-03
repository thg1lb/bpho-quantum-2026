import matplotlib.pyplot as plt, numpy as np
from scipy.integrate import quad

def planckSpectrum():
    
    # constant definitions
    kb = 1.381e-23
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
        
    plt.show()
    
planckSpectrum()
    

        
    
    
    
    