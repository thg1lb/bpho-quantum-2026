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
    
# movement
dt = 0.05

for frame in range(200):
    
    for i in range(numOfParticles):
        positions[i] += velocities[i] * dt
        x, y = positions[i]
        
        if (x - particleRadius <= 0 + particleRadius >= boxSize):
            velocities[i][0] *= -1
        
        if (y - particleRadius <= 0 + particleRadius >= boxSize):
            velocities[i][1] *= -1
        
        positions[i][0] = np.clip(positions[i][0], particleRadius, (boxSize - particleRadius))
        positions[i][1] = np.clip(positions[i][1], particleRadius, (boxSize - particleRadius))
        
        circles[i].center = positions[i]
        
       
        
    plt.pause(0.02)
        

# output/display
plt.show()


