import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np


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
    plt.scatter(freqCutoff, 0, s=30)
    plt.plot(freqs, V, label=material, linestyle = "--")
    plt.title("Photoelectric Effect: Multiple metals")
    plt.xlabel("Frequency / Hz (x10^15)")
    plt.ylabel("Stopping voltage / Volts")
    plt.legend() 
    
# for wsl (no display), save to png file
plt.savefig('output.png')





