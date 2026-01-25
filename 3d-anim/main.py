import numpy as np
import matplotlib.pyplot as plt
import time

fig, ax = plt.subplots()

# initial point
x = np.array([0])
y = np.array([0])

point, = ax.plot(x, y, marker="o")

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 5)
ax.set_title("Moving Point (manual)")

plt.show(block=False)

for i in range(5):
    y[0] = i
    point.set_data(x, y)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.5)

