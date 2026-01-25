"""
***************************************************************




        Basics of Animations -- 4




        Structure of an Animation
        



***************************************************************




        
    An animation has three main components:
    

1. Figure & Axis – where things are drawn


2. Init function – sets up the background


3. Update function – changes the plot frame-by-frame       


       

***************************************************************




        In this animation we move and rotate squares.
        

        

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




# define the squares to be animated
square1 = patches.Rectangle((0, 0), 1.5, 1.5, fc='red',  edgecolor='black')
square2 = patches.Rectangle((0, 0), 1.5, 1.5, fc='blue', edgecolor='red')
square3 = patches.Rectangle((0, 0), 2, 2,fill=False, edgecolor='brown')
square4 = patches.Rectangle((0, 0), 1, 1, fc='yellow', edgecolor='black')
square5 = patches.Rectangle((-1, -1), 2,  2, fc='maroon', edgecolor='black')


# add the squares to the Axes
axs.add_patch(square1)
axs.add_patch(square2)
axs.add_patch(square3)
axs.add_patch(square4)
axs.add_patch(square5)


# define the initialization function
def init():

    return square1, square2,  square3,  square4,  square5, 



# Update function -- plot the frames
def update(frame):
    
    t = (plt.matplotlib.transforms.Affine2D()
         .rotate_deg_around(0,  0,  frame*100)  # keep centered
         + axs.transData)
    
    square1.set_xy((frame, frame)) # Move diagonally
    square2.set_xy((frame, -frame)) # Move diagonally
    square3.set_xy((-1 + 3 * np.cos(frame), -1 + 3 * np.sin(frame))) # rotate CW
    square4.set_xy((-1 + 3 * np.cos(-frame), -1 + 3 * np.sin(-frame))) # rotate ACW
    square5.set_transform(t) # rotate about (0,  0)
    
    return square1, square2,  square3,  square4,  square5,  



# create the animation
ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=t,
                              init_func=init,
                              blit=True,
                              interval=50)



# set title and labels
plt.title("Moving_Rotating_Squares")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)



# save the animation as mp4
ani.save('Basics_4_Moving_Rotating_Squares.mp4')



# preview the animation
plt.show()























