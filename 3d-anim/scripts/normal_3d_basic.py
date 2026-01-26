#using main.py instead of jupyter-lab Ipython HTML
# **Note : Please download ffmpeg for this, using : sudo apt install ffmpeg {encoder for .mp4 files}**

import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.view_init(elev=60, azim=45)


point = ax.scatter([0], [0], [0])

def update(frame):
    z = frame * 0.1
    point._offsets3d = ([0], [0], [z])
    return point,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=200,
    interval=10
)

ani.save("/home/shubh/projects/3d-anim/assets/videos/changing_camera_angle.mp4", fps=30)

# *** Note : or if you dont want to install ffmpeg, you can also use inbuilt pillow library in jupyter, but instead of ".mp4" use ".gif" to store the output media. ***