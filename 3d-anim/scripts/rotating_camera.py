#using main.py instead of jupyter-lab Ipython HTML
# **Note : Please download ffmpeg for this, using : sudo apt install ffmpeg {encoder for .mp4 files}**

import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots(
    figsize=(6, 6),
    dpi=100,
    subplot_kw={"projection": "3d"}
)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_title("Moving point in z-axis")



# Create the point ONCE
point = ax.scatter([0], [0], [0])

def update(frame):  # callback function
    z = frame * 0.1
    point._offsets3d = ([0], [0], [z])
        # Camera motion
    ax.view_init(elev=frame, azim=frame)
    return point,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=360,      # controls animation length
    interval=20      # time between frames (ms)
)

ani.save("/home/shubh/projects/3d-anim/assets/videos/rotating_camera_angle.mp4", fps=30)

# *** Note : or if you dont want to install ffmpeg, you can also use inbuilt pillow library in jupyter, but instead of ".mp4" use ".gif" to store the output media. ***