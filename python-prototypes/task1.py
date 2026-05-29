# TASK #1. Random walk. Create a model of a random walk of
# N steps of size s. Each step is in a random direction, with angle
# theta from the horizontal chosen from a uniform distribution between 0 and
# 2pi radians.

import random, matplotlib.pyplot as plt, math, numpy

n = int(input("Please enter the number of steps: "))
s = int(input("Please enter the step size: "))

xPositions = [0]
yPositions = [0]

def random_walk():
    
    # set position at origin
    current_Xpos = 0
    current_Ypos = 0
    
    # loop for n-1 steps
    for i in range (n):
        
        # define theta
        theta = 2*math.pi*random.random() 
        
        # define new pos. based on previous pos. + step length/direction
        new_Xpos = current_Xpos + s*math.cos(theta)
        new_Ypos = current_Ypos + s*math.sin(theta)
        
        # add pos. values to respective arrays
        xPositions.append(new_Xpos)
        yPositions.append(new_Ypos)
        
        # update current pos. to match new pos.
        current_Xpos = new_Xpos
        current_Ypos = new_Ypos
        
        # debugging
        print()
        print(current_Xpos)
        print(current_Ypos)
        
def visuals():
        plt.plot(xPositions, yPositions)
        plt.show()
        
        
random_walk()
visuals()
        
    
    