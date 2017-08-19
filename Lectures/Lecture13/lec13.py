"""

        Lecture 13: Some Basic Probability and Plotting Data

"""




"""

     kopen heign doctron - physcist

     Causal Non - determinism : Caused by previous events

         Causal Non Determinism believed that not every event is based on the cause of a previous event.
         Which was disagree by Einstein and Schrodinger.
         Famously said by Einstein “God Does not play Dice.”

     Predictive Non - determinism :

         Our inability to make measurement of the physical world makes it impossible to make prediction of the future.
         So basically this means, things are not unpredictable, it just looks unpredictable because we do not have enough information.

    Stochastic Processes:

        The Processes of stochastic if it`s next state depends on both the previous state and some random element.
        


    Random:

        random.choice
        random.random : generates float number > 0 & < 1


"""
import random

""" Each roll is independent """
##def rollDie():
##    return random.choice([1,2,3,4,5,6])
##
##def testRoll(n=10):
##    result = ''
##    for i in range(n):
##        result = result + str(rollDie())
##        print result

"""
    What Fraction of possible results have property

    die - 1111111111 : 2**10 probability


    Data Visualization - Plotting
        Pylab - python library similar like matlab

        matplotlib.sourceforge.net : for detailed instructions and examples
"""

import pylab

#		x-coordinate, y-coordinate
#pylab.plot([1,2,3,4],[1,2,3,4])
#pylab.plot([1,4,2,3],[5,6,7,8])
#pylab.show()

#pylab.figure(1)
#pylab.plot([1,2,3,4], [1,2,3,4])
#pylab.figure(2)
#pylab.plot([1,4,2,3],[5,6,7,8])
#pylab.savefig('firstSaved')
#pylab.plot([5,6,7,10])
#pylab.savefig('secondSaved')
#pylab.show()



principal = 10000 ## initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values)

pylab.title("5% growth, Compounded Annually")
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')

pylab.show()
