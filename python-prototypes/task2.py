from matplotlib.patches import Circle
import matplotlib.pyplot as plt

# drawing the circle(s)
fig, ax = plt.subplots()

particle = Circle((0, 0), radius=1, fill=True)

ax.add_patch(particle)

# movement
position = 0
velocity = 0
dt = 0

# output/display
plt.show()


