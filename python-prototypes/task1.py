# TASK #1. Random walk. Create a model of a random walk of
# N steps of size s. Each step is in a random direction, with angle
# theta from the horizontal chosen from a uniform distribution between 0 and
# 2pi radians.

import random, matplotlib, math

n = int(input("Please enter the number of steps: "))
s = int(input("Please enter the step size: "))

xPositions = []
yPositions = []

def random_walk():
    
    current_Xpos = 0
    current_Ypos = 0
    
    for i in range (n):
        theta = 2*math.pi*random.random() 
        
        new_Xpos = current_Xpos + s*math.cos(theta)
        new_Ypos = current_Ypos + s*math.sin(theta)
        
        xPositions.append(new_Xpos)
        yPositions.append(new_Ypos)
        
        current_Xpos = new_Xpos
        current_Ypos = new_Ypos
        
        # debugging
        print()
        print(current_Xpos)
        print(current_Ypos)
        
        
random_walk()
        
    
    