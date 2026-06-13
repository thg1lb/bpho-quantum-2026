import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np

e0 = 8.8418782e-12
e = 1.602176620898e-19
h = 6.626e-34
c = 2.998e8
massE = 9.1093837e-31

spectralLines = {
    
    "Lyman": 1,
    "Balmer": 2,
    "Paschen": 3,
    "Brackett": 4,
    "Pfund": 5
     
}

for spectralLine, m in spectralLines.items():
 
 for n in range (m+1, 15):
     wavelength = ((8*(e0**2)*(h**3)*c)/(massE*(e**4)))*(((1/(m**2))-(1/(n**2)))**-1)
     wavelengthNm = wavelength * 1e9
    