import streamlit as st
import random
import matplotlib.pyplot as plt
import math

# TASK #1. Random walk. Create a model of a random walk of
# N steps of size s. Each step is in a random direction, with angle
# theta from the horizontal chosen from a uniform distribution between 0 and
# 2pi radians.

st.title("Task 1: Random walk model")

walks = st.slider("The number of walks", min_value=1, max_value=50, value=5)

n = st.slider("The number of steps", min_value=10, max_value=5000, value=500, step=10)

s = st.slider("The step size", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

xPositions = [0]
yPositions = [0]

fig, ax = plt.subplots()

# generates random walks based on user input
w = walks
        
while w > 0:   
    current_Xpos = 0
    current_Ypos = 0
    xPositions = [0]
    yPositions = [0]
                
    # loop for n-1 steps
    for i in range (n):
                        
        rand = random.random()
                            
        # define theta
        theta = 2*math.pi*rand
                            
        # define new pos. based on previous pos. + step length/direction
        new_Xpos = current_Xpos + s*math.cos(theta)
        new_Ypos = current_Ypos + s*math.sin(theta)
                            
        # add pos. values to respective arrays
        xPositions.append(new_Xpos)
        yPositions.append(new_Ypos)
                            
        # update current pos. to match new pos.
        current_Xpos = new_Xpos
        current_Ypos = new_Ypos    

    ax.plot(xPositions, yPositions)
    w -= 1
    
ax.set_title("Model of a random walk of N steps of size s.")
ax.set_xlabel("x-displacement")
ax.set_ylabel("y-displacement")
ax.grid(linestyle = '--')      
ax.set_aspect("equal", adjustable="box") 
                        
st.pyplot(fig, width="stretch")