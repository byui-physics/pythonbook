#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# This routine is the data generation routine.
# This type of code is called a generator, which
# is similar to a function with one exception:
# each time you call this function, it remembers
# where it was the last time you exited and picks
# up right where you left off.  
def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)  #The yield command it what makes this a generator, not a function.

# Routine to initialize the data to be plotted
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

# This routine will be called iteratively
# to update the plot object
def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    #If the data goes beyond the current
    # plot window, extend it.
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()

#import numpy as np
#from matplotlib import pyplot as plt
#from matplotlib import animation
#
## First set up the figure, the axis, and the plot element we want to animate
#plt.figure()
#plt.axes(xlim=(0, 2), ylim=(-2, 2))
#plt.plot([], [], lw=2)
#
#
#x = np.linspace(0,2,1000)
#for i in range(100):
#    plt.clf()
#    y = np.sin(2 * np.pi * (x - 0.01 * i))
#    plt.plot(x,y)
#    plt.draw()
#    plt.pause(.01)
