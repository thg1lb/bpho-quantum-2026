from matplotlib.patches import Circle
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

particle = Circle((0, 0), radius=1, fill=True)

ax.add_patch(particle)

plt.show()


