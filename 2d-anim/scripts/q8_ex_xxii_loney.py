"""
***************************************************




      Problem 8 - Ex XXII -- Pg 157
      

      The Elements of Coordinate Geometry


      S L Loney
      


***************************************************



      Whatever be the value of alpha,  prove that
      
      the locus of intersection of the straight

      lines

      xcos alpha + y sin alpha = A

      and

      xsin alpha - ycos alpha = B

      is a circle.




**************************************************
"""


# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches   # import patches 
import matplotlib.animation as animation


# set up the figure and axes
fig,  axs = plt.subplots()


# set up the axes 
axs.set_xlim(-6,  6)
axs.set_ylim(-6,  6)


#  show the axes in bold black
axs.axhline(0, color='black', linewidth=3)   
axs.axvline(0, color='black', linewidth=3) 


# set equal scales on both the axes
axs.set_aspect('equal', adjustable='box')


#  control the number of frames
t = np.linspace(0.01,  2*np.pi,   100)
xr = np.linspace(-6,  6,   100)

# set the values of A and B 
A = 2
B = 4


# initialize path line
xdata,  ydata = [],  []



# create the fixed circles
circle_A = axs.plot(A*np.cos(t),  A*np.sin(t),  'g-',  linewidth=3)
circle_B = axs.plot(B*np.cos(t),  B*np.sin(t),  'g-',  linewidth=3)



# create two lines,  a point and a path line
line1, = axs.plot([],  [],  'r-',  linewidth=2)
line2, = axs.plot([],  [],  'r-',  linewidth=2)
point,  = axs.plot([],  [],  'mo',  markersize=10)
path_line,  = axs.plot([], [],  linestyle='-', color='blue',  linewidth=2)





# define the init function
def init():
    xdata.clear()  # clear the previous line
    ydata.clear()  # clear the previous line
    path_line.set_data([],  [])

    return line1, line2, point, path_line,  



# reate the frames for the animation
def update(frame):

    xc = xr
    yc = (A - xr*np.cos(frame))/np.sin(frame)
    line1.set_xdata(xc)
    line1.set_ydata(yc)

    Xc = xr
    Yc = (xr*np.sin(frame) - B)/np.cos(frame)
    line2.set_xdata(Xc)
    line2.set_ydata(Yc)

    xp =  A*np.cos(frame)+B*np.sin(frame)
    yp = A*np.sin(frame)-B*np.cos(frame)
    point.set_xdata(xp)
    point.set_ydata(yp)

    
    xdata.append(xp)
    ydata.append(yp)
    path_line.set_data(xdata,   ydata)
    
    return line1,  line2, point, path_line,  



# create the animation
ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=t,
                              init_func=init,
                              blit=True,
                              interval=50)


# set title and labels
plt.title("q8_ex_xxii_s_l_loney")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)



# save the animation as mp4
ani.save('q8_ex_xxii_s_l_loney.mp4')


# preview the animation
plt.show()
    
