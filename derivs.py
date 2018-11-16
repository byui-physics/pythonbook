
# This function numerically differentiates the array y which
# represents the function y(x) for x-data points equally spaced
# dx apart.  The first and second derivatives are returned as
# the arrays yp and ypp which are the same length as the input
# array y.  Either linear or quadratic extrapolation is used
# to load the derivatives at the endpoints.  The user decides
# which to use by commenting out the undesired formula below.

from numpy import arange,cos,zeros_like
from matplotlib import pyplot

def derivs(y,dx):

    # load the first and second derivative arrays
    # at the interior points

    N=len(y)
    yp = zeros_like(y)  # Initialize array of zeros for first derivative
    ypp = zeros_like(y)  # Initialize array of zeros for second derivative

    yp[1:N-1]=(y[2:N]-y[0:N-2])/(2*dx)
    ypp[1:N-1]=(y[2:N]-2*y[1:N-1]+y[0:N-2])/(dx**2)

    # now use either linear or quadratic extrapolation to load the
    # derivatives at the endpoints


    # linear
    #yp[0]=2*yp[1]-yp[2]
    #yp[N-1]=2*yp[N-2]-yp[N-3]
    #ypp[0]=2*ypp[1]-ypp[2]
    #ypp[N-1]=2*ypp[N-2]-ypp[N-3]

    # quadratic
    yp[0]=3*yp[1]-3*yp[2]+yp[3]
    yp[N-1]=3*yp[N-2]-3*yp[N-3]+yp[N-4]
    ypp[0]=3*ypp[1]-3*ypp[2]+ypp[3]
    ypp[N-1]=3*ypp[N-2]-3*ypp[N-3]+ypp[N-4]

    return yp, ypp


# Build an array of function values
x=arange(0,10,.01)
y=cos(x)

# Then, since the function returns two arrays in the form
# yp,ypp, you would use it this way:
fp,fpp=derivs(y,.01)

# plot the approximate derivatives
pyplot.plot(x,fp,'r-',x,fpp,'b-')
pyplot.title('Approximate first and second derivatives')
pyplot.show()
