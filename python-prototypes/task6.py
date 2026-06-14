import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np

# constant definitions
e = 1.602176620898e-19
h = 6.626e-34
c = 2.998e8
massE = 9.1093837e-31

r = 65e-3

dValues = {
    
    "0.123 nm": 0.123e-9,
    "0.213 nm": 0.213e-9 
    
}

voltages = np.linspace(1000, 5000, 100)

# loop through d values
for label, d in dValues.items():
    
    # calculations
    wavelengths = h/np.sqrt(2*massE * e * voltages)
    phi = np.arcsin(wavelengths/(2*d))
    x = r * np.sin(2*phi)
    
    plt.plot(voltages/1000, x*1000, label=label)
    plt.title("Rings of radius x vs accelerating voltage")
    plt.xlabel("Voltage / kV")
    plt.ylabel("Ring radius / mm")
    plt.legend() 
    
    # task 6a - checkers
    xCheck = 1/np.sqrt(voltages)
    yCheck = np.sin(phi)
    plt.scatter(xCheck, yCheck, label=label)

    
plt.savefig('task6.png')