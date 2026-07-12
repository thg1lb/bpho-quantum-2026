import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np

e = 1.602176620898e-19
m = 9.1094e-31
h = 6.626e-34
a = 0.529e-10 # roughly from graph (Bohr radius) --> verify number
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
    plt.scatter(n, energiesInEv)
    plt.xlim(0, 3)
    plt.ylim(0, None)
        
    plt.savefig('task7a.png')
    
def probabilityVsX():
    
    for value in n:
        psi = np.sqrt(2/a) * np.sin(value*(np.pi)*(x/a))
        probDensity =  psi**2
        xAngstroms = x * 1e10
        
        plt.plot(xAngstroms, probDensity)
        plt.xlabel("x / angstroms")
        plt.ylabel("Probability density")
    
    plt.savefig('task7b.png')
    
probabilityVsX()
    
    