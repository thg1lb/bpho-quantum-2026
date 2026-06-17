import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np

m = 9.1094e-31
h = 6.626e-34
a = 0.529e-10 # roughly from graph (Bohr radius) --> verify number
hbar = h/(2*np.pi)
n = [1, 2, 3]     

energies  = []

# calculations
for value in n:
    E_n = ((hbar**2)*((np.pi)**2)*(value**2)) / (2*m*(a**2))
    energies.append(E_n)