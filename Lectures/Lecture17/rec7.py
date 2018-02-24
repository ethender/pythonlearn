"""

Recitation 7: Distributions, Monte Carlo, and Regressions

"""


"""

Distributions
1. Normal
2. Uniform
3. Exponential



Uniform
1/b-a
"""
import math
import pylab
import random


def show_discrete_uniform(a,b, num_points):
    points = []
    for s in range(num_points):
        points.append(random.randint(a,b))

    pylab.figure()
    pylab.hist(points,100,normed=True)
    pylab.title('Discrete uniform distributions with')
    pylab.show()

##show_discrete_uniform(1,100,100000)

def show_continous_uniform(a,b, num_points):
    points = []
    for s in range(num_points):
        points.append(random.uniform(a,b))

    pylab.figure()
    pylab.hist(points,100,normed=True)
    pylab.title('continous uniform distributions with')
    pylab.show()

##show_continous_uniform(0,1.0,100000)



"""
Normal (Gaussian)
mean  
"""
def frange(start, stop, step):
    l = []
    for i in range(int((stop-start)/step)):
        l.append(start+step*i)
    return l

def make_gaussian_pot(mu,sigma,num_points,show_ideal = True):
    points = []
    for m in range(num_points):
        points.append(random.gauss(mu,sigma))

    ideal_points_x = frange(mu - (sigma * 3) , mu +(sigma + 3), 0.0001)
    ideal_points_y = []
    for x in ideal_points_x:
        y = 1.0 / math.sqrt(2.0 * math.pi * sigma**2)*math.exp(-(x-mu)**2)
        ideal_points_y.append(y)
    pylab.figure()
    pylab.hist(points, 100, normed=True)

    if show_ideal:
        pylab.plot(ideal_points_x, ideal_points_y, 'r',lw=5)
        pylab.legend('Ideal curve, Random points')
    else:
        pylab.legend(['Random points'])
    pylab.title('Gaussian Distributions')
            
    
