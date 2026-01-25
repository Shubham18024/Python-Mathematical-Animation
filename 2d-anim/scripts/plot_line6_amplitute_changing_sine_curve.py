"""
***************************************************




      Rotate a stright line y = x about the origin



**************************************************
"""


# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# set up th figure and Axes
fig,  axs = plt.subplots()


# set up the axes 
axs.set_xlim(-10,  10)
axs.set_ylim(-10,  10)


#  show the axes in bold black
axs.axhline(0, color='black', linewidth=1)   
axs.axvline(0, color='black', linewidth=3) 


# set equal scales on both the axes
axs.set_aspect('equal', adjustable='box')





#  control the number of frames
t = np.linspace(-10,   10,   100)


# for plotting the fixed circle
u = np.linspace(-10,  10,   100)




# set up the geometric objects
straight_line,  = axs.plot([], [],  linestyle='-', color='blue',  linewidth=3)




# set up the init function
def init():
    
    straight_line.set_data([], [])
    
    return straight_line,   



# set up the function for frames
def update(frame):

    k = frame

    straight_line.set_data(u,  k*np.sin(u))
    
    return straight_line,   



# create the animation
ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=t,
                              init_func=init,
                              blit=True,
                              interval=50)


# set title and labels
axs.set_title("Amplitute Changing sine curve")
axs.set_xlabel("x")
axs.set_ylabel("y")
axs.grid(True)




# save the animation as mp4
ani.save('amplitute_changing_sine_curve.mp4')



# display the animation
plt.show()



