from matplotlib.patches import Circle
import numpy as np
import matplotlib.pyplot as plt

# settings
boxSize = 10
numOfParticles = 10
smallParticleRadius = 0.2
largeParticleradius = 0.8
smallParticleMass = 1.0
largeParticleMass = 10.0


# drawing the circle(s)
fig, ax = plt.subplots()

ax.set_xlim(0, boxSize)
ax.set_ylim(0, boxSize)
ax.set_aspect("equal")

# storing things
positions = []
velocities = []
circles = []

largePosition = np.array([boxSize/2, boxSize/2], dtype=float)
largeVelocity = np.array([0.0, 0.0])

# looping particle creation
for particle in range(numOfParticles):
    
    # axes
    x = np.random.uniform(smallParticleRadius, boxSize - smallParticleRadius)
    y = np.random.uniform(smallParticleRadius, boxSize - smallParticleRadius)
    
    largeCircle = Circle(largePosition, radius=largeParticleradius, fill=True)
    
    velocityX = np.random.uniform(-1, 1)
    velocityY = np.random.uniform(-1, 1)
    
    positions.append(np.array([x, y], dtype=float))
    velocities.append(np.array([velocityX, velocityY], dtype=float))

    circle = Circle((x, y), radius=smallParticleRadius, fill=True)
    
    circles.append(circle)
    ax.add_patch(largeCircle)
    ax.add_patch(circle)
    
# movement
dt = 0.05

for frame in range(200):
    
    for i in range(numOfParticles):
        positions[i] += velocities[i] * dt
        x, y = positions[i]
        
        if x - smallParticleRadius <= 0 + smallParticleRadius >= boxSize:
            velocities[i][0] *= -1
        
        if y - smallParticleRadius <= 0 + smallParticleRadius >= boxSize:
            velocities[i][1] *= -1
        
        positions[i][0] = np.clip(positions[i][0], smallParticleRadius, (boxSize - smallParticleRadius))
        positions[i][1] = np.clip(positions[i][1], smallParticleRadius, (boxSize - smallParticleRadius))
        
        circles[i].center = positions[i]
        
       
        
    plt.pause(0.02)
        

# output/display
plt.show()


