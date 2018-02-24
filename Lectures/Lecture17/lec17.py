
"""
    Lec - 17 : Curve Fitting
"""

import pylab

"""
        Physical reality
        Theoreticl model
        Computational models



        Hook`s Law: F= -kx
        Force = f
        k = spring constant
        x = object


        F = kx
        F = ma
        k = (m*g)/x
        
""" 
def getData(fileName):
    dataFile = open(fileName,'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d,m = line.split( )
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (distances,masses)

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 ## acc. due to gravity
    pylab.plot(xVals, yVals, 'bo', label='Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('[Force], (Newtons)')
    pylab.ylabel('Distance (metres)')

##plotData('Data/springData.txt')
##pylab.show()


"""
    Least squares fit
    i  = len(observations)-1 sum of i = 0 (observerd[i] - predicted[i])**2

polyfit(observedX, observedY, degree) - pylab use least squares fit

y = ax+b
"""


def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    pylab.plot(xVals, yVals, 'bo', label='Measured dispalcement')
    pylab.title('Measured Displacement of spring')
    pylab.xlabel('force [newtons]')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*pylab.array(xVals)+b
    k=1/a
    pylab.plot(xVals, estYVals, label='Linear fit, k='+str(round(k,5)))
    pylab.legend(loc='best')

    
##fitData('Data/springData.txt')
##pylab.show()


"""
Linear Regression
y = ax**2+bx+c :  for parabola
"""

def fitData1(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    pylab.plot(xVals,yVals,'bo',label='Measured dispalcement')
    pylab.title('Measured dispalcement of spring')
    pylab.xlabel('Force [newtons]')
    pylab.ylabel('Distance [meters]')
    a,b = pylab.polyfit(xVals,yVals,1)
    estYVals = a*pylab.array(xVals)+b
    k= 1/a
    pylab.plot(xVals, estYVals, label='Linear Fit')
    a,b,c,d = pylab.polyfit(xVals,yVals,3)
    estYVals = a*(xVals**3)+b*xVals**2+c*xVals+d
    pylab.plot(xVals, estYVals, label='Cubie fit')
    pylab.legend(loc='best')
    
    

##fitData1('Data/springData.txt')
##pylab.show()

def fitData2(fileName):
    xVals, yVals = getData(fileName)
    extX = pylab.array(xVals + [1.51])
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81
    extX = extX*9.81
    pylab.plot(xVals,yVals,'bo',label='Measured dispalcement')
    pylab.title('Measured dispalcement of spring')
    pylab.xlabel('Force [newtons]')
    pylab.ylabel('Distance [meters]')
    a,b = pylab.polyfit(xVals,yVals,1)
    extY = a*pylab.array(extX)+b
    #estYVals = a*pylab.array(xVals)+b
    #k= 1/a
    pylab.plot(extX, extY, label='Linear Fit')
    a,b,c,d = pylab.polyfit(xVals,yVals,3)
    estYVals = a*(extX**3)+b*extX**2+c*extX+d
    pylab.plot(extX, extY, label='Cubie fit')
    pylab.legend(loc='best')
    

##fitData2('Data/springData.txt')
##pylab.show()


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



def tryFits(fName):
    distances, heights = getTrajectoryData(fName)
    distances = pylab.array(distances)*36
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights+pylab.array(h)
    pylab.title('Trajectory of projectile (Mean of 4 trials)')
    pylab.xlabel('Inches from Launch point')
    pylab.ylabel('Inches Above Launch Point')
    meanHeights = totHeights/float(len(heights))
    pylab.plot(distances,meanHeights,'bo')
    a,b = pylab.polyfit(distances, meanHeights, 1)
    altitude = a*distances +b
    pylab.plot(distances, altitude, 'r', label = 'Linear Fit')
    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2)+b*distances+c
    pylab.plot(distances, altitude,'g',label='Quadratic Fit')
    pylab.legend()

##tryFits('Data/launcherData.txt')
##pylab.show()



"""
Coefficient of determination
R**2 = 1- (EE/MV)
"""
def rSquare(measured, estimated):
    EE = ((estimated -measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - EE/MV
def tryFital(fName):
    distances, heights = getTrajectoryData(fName)
    distances = pylab.array(distances)*36
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights * pylab.array(h)
    pylab.title('Trajectory of Projectile (Mean of 4 trials)')
    pylab.xlabel('Inches from Launch Point')
    
