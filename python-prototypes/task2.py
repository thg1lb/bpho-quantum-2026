from matplotlib.patches import Circle
import numpy as np
import matplotlib.pyplot as plt

# settings
numOfParticles = 10
boxSize = 10
particleRadius = 0.2

# drawing the circle(s)
fig, ax = plt.subplots()

ax.set_xlim(0, boxSize)
ax.set_ylim(0, boxSize)
ax.set_aspect("equal")

# storing things
positions = []
velocities = []
circles = []

# looping particle creation
for particle in range(numOfParticles):
    x = np.random.uniform(particleRadius, boxSize - particleRadius)
    y = np.random.uniform(particleRadius, boxSize - particleRadius)
    
    velocityX = np.random.uniform(-1, 1)
    velocityY = np.random.uniform(-1, 1)
    
    positions.append(np.array([x, y], dtype=float))
    velocities.append(np.array([velocityX, velocityY], dtype=float))

    circle = Circle((x, y), radius=particleRadius, fill=True)
    
    circles.append(circle)
    ax.add_patch(circle)

# output/display
plt.show()


