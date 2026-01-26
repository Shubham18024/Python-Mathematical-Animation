import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots(
    figsize=(5, 5),
    subplot_kw={"projection": "3d"}
)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

# Initial point (object space)
p0 = np.array([3, 0, 0])

point = ax.scatter([p0[0]], [p0[1]], [p0[2]])

def update(frame):
    theta = np.deg2rad(0.5*frame)

    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])

    p = Rz @ p0
    point._offsets3d = ([p[0]], [p[1]], [p[2]])

    return point,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=720,
    interval=30
)

ani.save("/home/shubh/projects/3d-anim/assets/videos/rotating_object.mp4", fps=60)

# *** Note : or if you dont want to install ffmpeg, you can also use inbuilt pillow library in jupyter, but instead of ".mp4" use ".gif" to store the output media. ***
