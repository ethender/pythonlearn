"""

    Lecture 14: Sampling and Monte Carlo Simulation

"""


import random, pylab

##principal = 10000.0 #initial investment
##interestRate = 0.05
##years = 20
##values = []
##for i in range(years + 1):
##    values.append(principal)
##    principal += principal*interestRate
##pylab.plot(values)
####pylab.show()
##
##pylab.title('5% Growth, compounded Annually')
##pylab.xlabel('Years of compounding')
##pylab.ylabel('Value of Prinicipal ($)')
##pylab.show()


"""
    probability never be 1

    1 means possible
    0 means not possible

    (5/6)**10 not getting chance contain 1 in a six sided die rolling 10 times
    (1-(5/6)**10) getting chance contain 1 in a six sided die rolling 10 times

    what is probability getting 2 sixes <6,6>

    what is the probability of not rolling 6 on one die is 1/6
    another die is 1/6
    total = 1/36 - probability of getting double sixes.
    1-1/36 = (35-26) not getting probability 
    (35/36)**24 getting doubles sixes probaility in 24 rolls.
"""


##def rollDie():
##    return random.choice([1,2,3,4,5,6])
##
##def testRoll(n=10):
##    result = ''
##    for i in range(n):
##        result = result + str(rollDie())
##    print(result)
##
##def checkPascal(numTrials = 100000):
##    yes = 0.0
##    for i in range(numTrials):
##        for j in range(24):
##            d1 = rollDie()
##            d2 = rollDie()
##            if d1 == 6 and d2 == 6:
##                yes += 1
##                break
##    print 'Probability of losing = '+str(1.0 - yes/numTrials)
##checkPascal()
##print((35.0/36.0)**24)





"""
    Monte carlo simulation

    Inferential statistics
        Random sample tends to exhibit. The same properties as population 

"""


##def flip(numFlips):
##    heads = 0
##    for i in range(numFlips):
##        if random.random() < 0.5:
##            heads += 1
##    return heads/float(numFlips)
##print(flip(10))



"""
    Law of large numbers

    Repeated independet tests with same number actual probability, p ,
    Chance that fraction of times outcome occurs converges to p as trials goes to infinity 

"""

def flipPlot(minExp, maxExp):
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
##    pylab.title('Difference between Head and Tails')
##    pylab.xlabel('Number of flips')
##    pylab.ylabel('Abs(#Heads - #Tails)')
##    pylab.plot(xAxis, diffs)
##    pylab.figure()
##    pylab.plot(xAxis,ratios)
##    pylab.title('Head/Tails ratios')
##    pylab.xlabel('Number of flips')
##    pylab.ylabel('Heads/Tails')
    pylab.figure()
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis, ratios, 'bo')
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of flips')
    pylab.ylabel('Heads/Tails')
    pylab.semilogx()


flipPlot(4,20)
pylab.show()
