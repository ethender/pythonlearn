##
##
##Lecture 12: Introduction to simulation and Random Walks
##
##
##
##
##



##Difference between yield & return
##
##Yield is a generator 
##      - is a function that remembers
##        the point in function body where
##        it last returned. plus local variables.
##
##Return : It just return the value. where it occurred.
##
##

##
##Analytic methods:
##      - predict behaviour, given initial conditions & parameters.
##
##Simulation methods:
##  - systems not mathematical trackable
##  - successively refining series of simulation
##  - Easier useful intermediate results
##  - computers


##build a model,
##  - give useful information about behaviour of a system
##  - approximation of reality
##  - simulation models are descriptive, not prescriptive
##
##
##



##Brownian motion is an example of a random walk
##
##Simulation of drunken student walking on the field after 1000 setps where he will be.
##             Dist  Prob
##    1 step = 1     1
##    2 step = 0     1/4
##             root2 2/4
##             2     1/4
##
##    3 step = 1     1/4
##             1     1/4
##             root5 1/4
##             1     1/16
##             root5 1/16

##  1 step  1
##  2 steps 1.2
##  3 steps 1.4


##Model we need 
##  Drunk
##  Field
##  Location

import random

class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self,deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<'+str(self.x)+", "+str(self.y)+" >"


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self,drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk nit in field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist,yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')

        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name

    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
        return random.choice(stepChoices)
    def __str__(self):
        return 'This drunk is named '+self.name


def walk(f,d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = Drunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer,origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTest(numTrials):
    for numSteps in [10, 100, 1000, 100000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of '+str(numSteps)+ ' steps'
        print ' Mean =',sum(distances)/len(distances)
        print ' Max =',max(distances),' Min= ',min(distances)
