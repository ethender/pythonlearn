"""

Lec 18 : Optimization Problems and Algorithms

"""
"""

r**2 == 1 : Model is explains all varialbility of data
r**0 == 0 : no linear relationship of data


Compute Speed of  arrow:
1. Trajectory given by, y = ax**2+bx+c
    Peak of parabola occurs halfway between launch and target, call this xMild

    yPeak =x*xMid**2 + b*xMid+c

2. Time to fall from yPeak to target (height = 0),
    purely a function of acceleration due to gravity.

    t= sqrt(2*yPeak/g)
    g = gravity
3. This is also the time required to go from xMid to xMax.
    Can easily compute the average horizontal speed over that distance.
    If we assume no drag, that speed is horizontal speed at which projectile hits target.
"""

import pylab


def rSquare(measured, estimated):
    """measured: one dimensional array of measured values
       estimate: one dimensional array of predicted values"""
    EE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - EE/MV

def getTrajectoryData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    heights1, heights2, heights3, heights4 = [],[],[],[]
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, h1, h2, h3, h4 = line.split()
        distances.append(float(d))
        heights1.append(float(h1))
        heights2.append(float(h2))
        heights3.append(float(h3))
        heights4.append(float(h4))
    dataFile.close()
    return (distances, [heights1, heights2, heights3, heights4])


def getXSpeed(a,b,c,minX,maxX):
    xMid = (maxX - minX)/2.0
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*12 #accel of gravity in inches/sec/sec
    t = (2.0*yPeak/g)**0.5
    return xMid/(t*12.0)

def processTrajectories(fName):
    distances, heights = getTrajectoryData(fName)
    distances = pylab.array(distances)*36
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    pylab.title('Trajectory of Projectile (Mean of 4 Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    meanHeights = totHeights/len(heights)
    pylab.plot(distances, meanHeights, 'bo')
    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2) +  b*distances + c
    speed = getXSpeed(a, b, c, distances[-1], distances[0])
    pylab.plot(distances, altitudes, 'g',
               label = 'Quad. Fit' + ', R2 = '
               + str(round(rSquare(meanHeights, altitudes), 2))
               + ', Speed = ' + str(round(speed, 2)) + 'feet/sec')
    pylab.legend()
##processTrajectories('launcher_data.txt')
##pylab.show()




"""
1. start with an experiment
2. Use computation to find and evaluate 
3. Used some theory + analysis + computation
to derive a consequence of model



Optimization Problems
 1. An Objective Function
 2. A set of constraints

 Problem reduction

Greedy Algorithm:

        At each step choose locally optimal solution

        0/1 knapsnack problem: because either we have take 1 or none 

"""


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result


def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items


##
##Efficiency of greedy algorithm
## order(len(Item)* log(len(Items)))
## order(len(Items))
## equals to linear
##
def greedy(Items, maxWeight, keyFcn):
    assert type(Items) == list and maxWeight >= 0
    ItemsCopy = sorted(Items, key=keyFcn, reverse = True)
    result = []
    totalVal = 0.0
    totalWeight = 0.0
    i = 0
    while totalWeight < maxWeight and i < len(Items):
        if (totalWeight + ItemsCopy[i].getWeight()) <= maxWeight:
            result.append((ItemsCopy[i]))
            totalWeight += ItemsCopy[i].getWeight()
            totalVal += ItemsCopy[i].getValue()
        i += 1
    return (result, totalVal)


def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def testGreedy(Items, constraint, getKey):
    taken, val = greedy(Items, constraint, getKey)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

def testGreedys(maxWeight = 20):
    Items = buildItems()
    print('Items to choose from:')
    for item in Items:
        print '  ', item
    print 'Use greedy by value to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, value)
    print 'Use greedy by weight to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, weightInverse)
    print 'Use greedy by density to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, density)


##
##How to solve Problems:
## 1. Item = <value,weight> 
## 2. W as maximum weight
## 3. I as vector of a valuable items
## 4. V as vector v[i] = 1 => I[i] has been taken
##
##What happen worst cases
##  1. Enumerate all possibilities
##  2. Choose best that meets constraint
def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and n >=0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n//2
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr

def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)
    templates = []
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset

def chooseBest(pset, constraint, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)

def testBest():
    Items = buildItems()
    pset = genPset(Items)
    taken, val = chooseBest(pset, 20, Item.getValue, Item.getWeight)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

    
