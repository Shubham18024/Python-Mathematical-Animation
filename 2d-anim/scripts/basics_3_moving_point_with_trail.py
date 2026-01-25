"""
***************************************************************




        Basics of Animations -- 3




        Structure of an Animation
        



***************************************************************




        
    An animation has three main components:
    

1. Figure & Axis – where things are drawn


2. Init function – sets up the background


3. Update function – changes the plot frame-by-frame       


       

***************************************************************




        In this animation we animate the trail(path) of a point 

        moving along a line y = x.
        

        

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


# variables to store the points of the path
# initialize the path to be animated
xdata,  ydata = [],  []


# define the point and the path to be animated
point,  = axs.plot([],  [],  'ro',   markersize=10)
path_line,  = axs.plot([], [],  'b-',  linewidth=2)



# define the initialization function
def init():
    xdata.clear()  # clear the previous line
    ydata.clear()  # clear the previous line
    path_line.set_data([],  [])
    
    point.set_data([],  [])
    
    return path_line, point, 



# Update function -- plot the frames
def update(frame):
    x = frame
    y = frame
    xdata.append(x)
    ydata.append(y)
    point.set_data([x],   [y])
    path_line.set_data(xdata,   ydata)

    return path_line, point,



# create the animation
ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=t,
                              init_func=init,
                              blit=True,
                              interval=50)



# set title and labels
plt.title("Moving Point With Trail Along the line y = x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)



# save the animation as mp4
ani.save('Basics_3_Moving_Point_With_Trail.mp4')



# preview the animation
plt.show()



"""
***************************************************************


                    Exercises


                    

1. Animate the path of a point moving along the line x = 2


2. Animate the path of a point moving along the line y = 2


3. Animate the path of a point moving along the line y = 2x


4. Animate the path of a point moving along the curve y = x^2


5. Animate the path of a point moving along the curve y = x^3


6. Animate the path of a point moving along the curve y = sin x


7. Animate the path of a point moving along the circle x^2 + y^2 = 1


8. Animate the path of a point moving along the ellipse x^2/ 4 + y^2 = 1



9. Animate two  paths of apoints -- one point moving along the line x = 2

and another moving along the line y = 2 with different colors.



10. Animate four  paths of points -- each point moving along the curves

y = x,  x^2,  x^3 and y = x^4.     

        

***************************************************************
"""




















