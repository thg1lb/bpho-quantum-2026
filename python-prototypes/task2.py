from matplotlib.patches import Circle
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# settings
boxSize = 10
numOfParticles = 20
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
trail = []

largePosition = np.array([boxSize/2, boxSize/2], dtype=float)
largeVelocity = np.array([0.0, 0.0])
largeCircle = Circle(largePosition, radius=largeParticleradius, fill=True)
ax.add_patch(largeCircle)

# looping particle creation
for particle in range(numOfParticles):
    
    # axes
    x = np.random.uniform(smallParticleRadius, boxSize - smallParticleRadius)
    y = np.random.uniform(smallParticleRadius, boxSize - smallParticleRadius)
    

    
    velocityX = np.random.uniform(-1, 1)
    velocityY = np.random.uniform(-1, 1)
    
    positions.append(np.array([x, y], dtype=float))
    velocities.append(np.array([velocityX, velocityY], dtype=float))

    circle = Circle((x, y), radius=smallParticleRadius, fill=True)
    
    circles.append(circle)
    ax.add_patch(circle)
    
# movement
dt = 0.2

# frame generation
for frame in range(500):
    
    for i in range(numOfParticles):
        positions[i] += velocities[i] * dt
        x, y = positions[i]
        
        if x - smallParticleRadius <= 0 and velocities[i][0] < 0:
            velocities[i][0] *= -1

        elif x + smallParticleRadius >= boxSize and velocities[i][0] > 0:
            velocities[i][0] *= -1

        if y - smallParticleRadius <= 0 and velocities[i][1] < 0:
            velocities[i][1] *= -1

        elif y + smallParticleRadius >= boxSize and velocities[i][1] > 0:
            velocities[i][1] *= -1
            
        largePosition += largeVelocity * dt
        
        if largePosition[0] - largeParticleradius <= 0 and largeVelocity[0] < 0:
            largeVelocity[0] *= -1

        elif largePosition[0] + largeParticleradius >= boxSize and largeVelocity[0] > 0:
            largeVelocity[0] *= -1

        if largePosition[1] - largeParticleradius <= 0 and largeVelocity[1] < 0:
            largeVelocity[1] *= -1

        elif largePosition[1] + largeParticleradius >= boxSize and largeVelocity[1] > 0:
            largeVelocity[1] *= -1

        largePosition[0] = np.clip(
            largePosition[0],
            largeParticleradius,
            boxSize - largeParticleradius
        )

        largePosition[1] = np.clip(
            largePosition[1],
            largeParticleradius,
            boxSize - largeParticleradius
        )
        
        positions[i][0] = np.clip(positions[i][0], smallParticleRadius, (boxSize - smallParticleRadius))
        positions[i][1] = np.clip(positions[i][1], smallParticleRadius, (boxSize - smallParticleRadius))
        
        circles[i].center = positions[i]
        
        # particle collision
        difference = positions[i] - largePosition
        centerDistance = np.linalg.norm(difference)
        
        # trace large particle movement
        trail.append(largePosition.copy())
        
        if 0 < centerDistance <= smallParticleRadius + largeParticleradius:

            # find collision direction and speed
            collisionNormal = difference / centerDistance
            relativeVelocity = velocities[i] - largeVelocity
            
            # dot product to see if movement is towards eachother
            speedAlongNormal = np.dot(relativeVelocity, collisionNormal)
            
            if speedAlongNormal < 0:
                impulse = (-(2*speedAlongNormal) / ((1/smallParticleMass) + (1/largeParticleMass)))

                overlap = smallParticleRadius + largeParticleradius - centerDistance
                
                positions[i] += collisionNormal * (overlap / 2)
                largePosition -= collisionNormal * (overlap / 2)
                
                velocities[i] += (impulse/smallParticleMass) * collisionNormal
                largeVelocity -= (impulse/largeParticleMass) * collisionNormal
        
       
    largePosition += largeVelocity * dt
    largeCircle.center = largePosition 
    plt.pause(0.02)
        

# output/display
plt.show()


