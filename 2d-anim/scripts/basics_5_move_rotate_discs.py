"""
***************************************************************




        Basics of Animations -- 5




        Structure of an Animation
        



***************************************************************




        
    An animation has three main components:
    

1. Figure & Axis – where things are drawn


2. Init function – sets up the background


3. Update function – changes the plot frame-by-frame       


       

***************************************************************




        In this animation we move and rotate discs.
        

        

***************************************************************
"""




# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches   # import patches
import matplotlib.animation as animation



# set up the figure and axes
fig, axs = plt.subplots()


# set up the axes 
axs.set_xlim(-6,  6)
axs.set_ylim(-6,  6)


#  show the axes in bold black
axs.axhline(0, color='black', linewidth=3)   
axs.axvline(0, color='black', linewidth=3) 


# set equal scales on both the axes
axs.set_aspect('equal', adjustable='box')


#  control the number of frames
t = np.linspace(-6,  6,   100)




# define the discs to be animated
disc1 = patches.Circle((0, 0),  1, fc='red',  edgecolor='black')
disc2 = patches.Circle((0, 0),  0.75, fc='brown',  edgecolor='black')
disc3 = patches.Circle((0, 0),  1.25, fc='green',  edgecolor='black')
disc4 = patches.Circle((0, 0),  1.5, fc='blue',  edgecolor='black')

# add the discs to the Axes
axs.add_patch(disc1)
axs.add_patch(disc2)
axs.add_patch(disc3)
axs.add_patch(disc4)


# define the initialization function
def init():

    return disc1,  disc2,  disc3, disc4, 



# Update function -- plot the frames
def update(frame):
    
    disc1.set_radius(frame) # change radius

    x, y = disc2.center
    x = frame
    y = frame
    
    disc2.center = (x,  y)
    disc3.center = (x,  0)
    disc4.center = (2*np.cos(frame),  2*np.sin(frame))
    
    return disc1,  disc2,  disc3,  disc4, 



# create the animation
ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=t,
                              init_func=init,
                              blit=True,
                              interval=50)



# set title and labels
plt.title("Moving_Rotating_Discs")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)



# save the animation as mp4
ani.save('Basics_5_Moving_Rotating_Discs.mp4')



# preview the animation
plt.show()























