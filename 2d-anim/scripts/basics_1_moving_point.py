"""
***************************************************************




        Basics of Animations -- 1




        Structure of an Animation
        



***************************************************************




        
    An animation has three main components:
    

1. Figure & Axis – where things are drawn


2. Init function – sets up the background


3. Update function – changes the plot frame-by-frame       


       

***************************************************************




        In this animation we plot a point and animate

        it along a line y = x.
        

        

***************************************************************
"""




# import the libraries
import numpy as np
import matplotlib.pyplot as plt
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


# initialize the point to be animated
# define the object to be animated
point,  = axs.plot([],  [],  'ro',   markersize=10)



# define the initialization function
def init():
    point.set_data([],  [])

    return point,



# Update function -- plot the frames
def update(frame):
    point.set_data([frame],   [frame])

    return point,



# create the animation
ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=t,
                              init_func=init,
                              blit=True,
                              interval=50)



# set title and labels
plt.title("Point Moving Along the line y = x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)



# # save the animation as mp4
# ani.save('Basics_1_Point_Moving.mp4')



# preview the animation
plt.show()



"""
***************************************************************


                    Exercises


                    

1. Animate a point moving along the line x = 2


2. Animate a point moving along the line y = 2


3. Animate a point moving along the line y = 2x


4. Animate a point moving along the curve y = x^2


5. Animate a point moving along the curve y = x^3


6. Animate a point moving along the curve y = sin x


7. Animate a point moving along the circle x^2 + y^2 = 1


8. Animate a point moving along the ellipse x^2/ 4 + y^2 = 1



9. Animate two points -- one point moving along the line x = 2

and another moving along the line y = 2 with different colors.



10. Animate four points -- each point moving along the curves

y = x,  x^2,  x^3 and y = x^4.     

        

***************************************************************
"""




















