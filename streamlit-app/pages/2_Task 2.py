import streamlit as st
import time
from matplotlib.patches import Circle
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

#TASK #2: Consider N small particles of mass m and radius r moving randomly, and one large particle of mass M and radius R. Determine the motion of the large particle if it starts from rest. Ideally animate it!

st.subheader("Brownian Motion Simulation")

st.caption(
    "Random collisions with the surrounding smaller particles transfer momentum "
    "to the larger particle, producing an irregular Brownian-like trajectory. "
    "The trail shows the path followed by the large particle."
)

# settings
boxSize = 10
numOfParticles = st.sidebar.slider("Number of particles", min_value=10, max_value=100, value=20)
smallParticleRadius = 0.2
largeParticleradius = 0.8
smallParticleMass = 1.0
largeParticleMass = 10.0

# time interval - used to update particle pos.
dt = st.sidebar.slider("Time step", min_value=0.01, max_value=0.5, value=0.2)

# display settings
fig, ax = plt.subplots()

ax.set_xlim(0, boxSize)
ax.set_ylim(0, boxSize)
ax.set_aspect("equal")

# storing things
positions = []
velocities = []
circles = []
trail = [] # large particle positions in order to trace its path

# large particle xtra settings
largePosition = np.array([boxSize/2, boxSize/2], dtype=float)
largeVelocity = np.array([0.0, 0.0])
largeCircle = Circle(largePosition, radius=largeParticleradius, fill=True, zorder=3)
ax.add_patch(largeCircle)

placeholder = st.empty()

if st.button("Start sim"):

    # looping particle creation
    for particle in range(numOfParticles):
        
        # axes
        x = np.random.uniform(smallParticleRadius, boxSize - smallParticleRadius)
        y = np.random.uniform(smallParticleRadius, boxSize - smallParticleRadius)
        
        velocityX = np.random.uniform(-1, 1)
        velocityY = np.random.uniform(-1, 1)
        
        positions.append(np.array([x, y], dtype=float))
        velocities.append(np.array([velocityX, velocityY], dtype=float))

        circle = Circle((x, y), radius=smallParticleRadius, fill=True, zorder=2)
        
        circles.append(circle)
        ax.add_patch(circle)
        
    trailLine, = ax.plot([], [], linewidth=1, color="red", zorder=10)


    # frame generation when running sim
    for frame in range(500):
        
        for i in range(numOfParticles):
            
            # updates pos. using velocity * time step
            positions[i] += velocities[i] * dt
            x, y = positions[i]
            
            # small particle wall collisions
            # reverses a given velocity component when the particle reaches a wall
            # (models an elastic collision)
            if x - smallParticleRadius <= 0 and velocities[i][0] < 0:
                velocities[i][0] *= -1

            elif x + smallParticleRadius >= boxSize and velocities[i][0] > 0:
                velocities[i][0] *= -1

            if y - smallParticleRadius <= 0 and velocities[i][1] < 0:
                velocities[i][1] *= -1

            elif y + smallParticleRadius >= boxSize and velocities[i][1] > 0:
                velocities[i][1] *= -1
                
            # large particle wall collisions
            if largePosition[0] - largeParticleradius <= 0 and largeVelocity[0] < 0:
                largeVelocity[0] *= -1

            elif largePosition[0] + largeParticleradius >= boxSize and largeVelocity[0] > 0:
                largeVelocity[0] *= -1

            if largePosition[1] - largeParticleradius <= 0 and largeVelocity[1] < 0:
                largeVelocity[1] *= -1

            elif largePosition[1] + largeParticleradius >= boxSize and largeVelocity[1] > 0:
                largeVelocity[1] *= -1

            # to keep the large particle in the container
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
            
            # to keep the small particles in the container
            positions[i][0] = np.clip(positions[i][0], smallParticleRadius, (boxSize - smallParticleRadius))
            positions[i][1] = np.clip(positions[i][1], smallParticleRadius, (boxSize - smallParticleRadius))
            
            # update pos. of particle (graphically)
            circles[i].center = positions[i]
            
            # particle collision detection
            difference = positions[i] - largePosition # vector from large to small particle
            centerDistance = np.linalg.norm(difference)
            
            # collision occurs when distance between centres
            # is less than or equal to sum of the radii
            if 0 < centerDistance <= smallParticleRadius + largeParticleradius:

                # find collision direction and speed
                collisionNormal = difference / centerDistance
                relativeVelocity = velocities[i] - largeVelocity
                
                # dot product to see if movement is towards eachother
                speedAlongNormal = np.dot(relativeVelocity, collisionNormal)
                
                # only resolves collision if particles are moving towards eachother
                if speedAlongNormal < 0:
                    impulse = (-(2*speedAlongNormal) / ((1/smallParticleMass) + (1/largeParticleMass)))

                    # fixes overlap
                    overlap = smallParticleRadius + largeParticleradius - centerDistance
                    
                    positions[i] += collisionNormal * (overlap / 2)
                    largePosition -= collisionNormal * (overlap / 2)
                    
                    velocities[i] += (impulse/smallParticleMass) * collisionNormal
                    largeVelocity -= (impulse/largeParticleMass) * collisionNormal
                
        # updates large particle after all collisions in frame
        largePosition += largeVelocity * dt
        largeCircle.center = largePosition 
        
        # trace large particle movement
        trail.append(largePosition.copy())
        
        trailArray = np.array(trail)
        trailLine.set_data(trailArray[:,0], trailArray[:,1])
        
        # redraws simulation frame as png
        buffer = BytesIO()
        fig.savefig(buffer, format="png", bbox_inches="tight")
        buffer.seek(0)

        placeholder.image(buffer.getvalue())

        time.sleep(0.02)

# allows user to reset simulation if needed
if st.button("Reset"):
            st.rerun()