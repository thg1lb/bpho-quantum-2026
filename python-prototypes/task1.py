# TASK #1. Random walk. Create a model of a random walk of
# N steps of size s. Each step is in a random direction, with angle
# theta from the horizontal chosen from a uniform distribution between 0 and
# 2pi radians.

import random, matplotlib.pyplot as plt, math, numpy

walks = int(input("Please enter how many walks you would like displayed: "))
n = int(input("Please enter the number of steps: "))
s = int(input("Please enter the step size: "))
walkCounter = 0

xPositions = [0]
yPositions = [0]

# generates random walks based on user input
def random_walk():
        
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
                        
                # plotting       
                plt.plot(xPositions, yPositions)
                plt.title("Model of a random walk of N steps of size s.")
                plt.xlabel("x-axis")
                plt.ylabel("y-axis")
                plt.grid(linestyle = '--')       
                w -= 1
                        
        plt.show()
        
# function calls   
random_walk()
        
    
    