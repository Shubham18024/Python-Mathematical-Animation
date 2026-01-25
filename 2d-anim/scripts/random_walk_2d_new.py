"""
***************************************************************




            random_walk_2d_new
       
       
    
        

        

***************************************************************
"""




# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



# set up the figure and axes
fig, axs = plt.subplots()


# frame x and y limits
a = 7



# set up the axes 
axs.set_xlim(-a,  a)
axs.set_ylim(-a,  a)


#  show the axes in bold black
axs.axhline(0, color='black', linewidth=3)   
axs.axvline(0, color='black', linewidth=3) 


# set equal scales on both the axes
axs.set_aspect('equal', adjustable='box')


#  control the number of frames
N = 100



# variables to store the points of the path
# initialize the path to be animated
x,  y = [0],  [0]


# define the path to be animated
path_line,  = axs.plot([], [],  'r-',  linewidth=2)



# define the initialization function
def init():
    x.clear()  # clear the previous line
    y.clear()  # clear the previous line

    
    x.append(0)  # reset x0 = 0
    y.append(0)  # reset y0 = 0
    
    path_line.set_data([],  [])
    
    return path_line,



# Update function -- plot the frames
# frame starts from 0
def update(frame):
    xold = x[frame]
    yold = y[frame]

    
    rnd = np.random.randint(1,  5)
    if rnd == 1:
        xnew = xold + 1
        ynew = yold
    elif rnd == 2:
        xnew = xold - 1
        ynew = yold
    elif rnd == 3:
        xnew = xold
        ynew = yold + 1
    else:
        xnew = xold
        ynew = yold - 1
        
    x.append(xnew)
    y.append(ynew)
    
    path_line.set_data(x,   y)

    return path_line,



# create the animation
ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=N,
                              init_func=init,
                              blit=True,
                              interval=50)



# set title and labels
plt.title("random_walk_2d_new")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)



# save the animation as mp4
ani.save('random_walk_2d_new.mp4')



# preview the animation
plt.show()


