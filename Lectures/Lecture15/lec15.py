"""

    Lecture 15: Statistical Thinking

"""

"""

    How many samples are needed to have confidence in result

    Variants - measure of how much spread there is in possible outcomes

    Standard deviation - The Fraction of values close to mean
        Note: reach out for formulae.

    Mean - sum(x[0]+x[1])/len(x)
"""
import random, pylab


def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def flipPlot(minExp, maxExp, numTrials):
    meanRatios = []
    meanDiffs = []
    ratiosSDs = []
    diffsSDs = []
    xAxis = []
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads = 0
            for n in range(numFlips):
                if random.random() < 0.5:
                    numHeads += 1
            numTails = numFlips - numHeads
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    pylab.plot(xAxis, meanRatios, 'bo')
    pylab.title('Mean Head/Tails Ratios ('+str(numTrials)+' Trails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean Heads/Tails')
    pylab.semilogx()
    pylab.figure()

    
    pylab.plot(xAxis, ratiosSDs,'bo')
    pylab.title('SD Heads/Tails ratios ('+str(numTrials)+' Trials')
    pylab.xlabel('Number of flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()

    
    pylab.title('Mean abs(#Heads - #Tails) ('+str(numTrials)+'Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean abs(#Heads - #Tails)')
    pylab.plot(xAxis,meanDiffs,'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()

    pylab.plot(xAxis,diffsSDs,'bo')
    pylab.title('SD abs(#Heads - #Tails) ('+str(numTrials)+' Trials')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()


##flipPlot(4,20,20)
##pylab.show()
##    
"""

    Coefficient of variation - standard deviation / mean

    If < 1,  low variance
    Cannot be used for confidence intervals
    
"""
    
    
def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1.0
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    return fracHeads

def labelPlot(nf, nt, mean, ad):
    pylab.title(str(nt)+' trials of '+str(nf)+' flips each')
    pylab.xlabel('Fraction of heads')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin+(xmax-xmin)*0.02,(ymax-ymin)/2,'Mean ='+str(round(mean,6))+'\nSD ='+str(round(ad,6)))


def makePlots(nf1, nf2, nt):
    """
        nt = number of trials per experiment
        nf1 = number of flips 1st experiment
        nf2 = number of flips 2nd experiment
    """
    fracHeads1 = flipSim(nf1, nt)
    mean1 = sum(fracHeads1)/float(len(fracHeads1))
    sd1 = stdDev(fracHeads1)
    pylab.hist(fracHeads1, bins = 20)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    labelPlot(nf1,nt,mean1,sd1)
    pylab.figure()
    fracHeads2 = flipSim(nf2, nt)
    mean2 = sum(fracHeads2)/float(len(fracHeads2))
    sd2 = stdDev(fracHeads2)
    pylab.hist(fracHeads2, bins=20)
    pylab.hist(fracHeads2, bins=20)
    pylab.xlim(xmin, xmax)
    ymin, ymax = pylab.ylim()
    labelPlot(nf2, nt, mean2, sd2)

##L = [1,2,3,3,3,4]
##pylab.hist(L, bins=7)
##makePlots(100, 1000, 100000)
##pylab.show()

"""

    Normal distribution - Peaks at mean Falls of symmetrically -
    Shape of Normal distribution - bell shape
    Normal distribution is also called Bell Curve 

    Normal Distribution frequently uses for 2 reasons
    1. Nice mathematical properties
    2. Many naturally occurring instances (or) examples

    charactersized by mean and standard deviation
    confidence intervals - range likely to contain unknown value and confidence level
                            that values lies within range
        ex: political candidate get votes - 52% +- 4% = 48% or 56%



    Empirical rule -
        68%   of data within 1 standard deviation of mean
        95%   of data within 2 standard deviation of mean
        99.7% of data within 3 standard deviation of mean

    Standard Error - estimate of standard deviation
    p = % sampled ,
    n = sample size
    stand error se = ((p*(100-p)/n))**0.5 

"""

def poll(n, p):
    votes = 0.0
    for i in range(n):
        if random.random() < p/100.0:
            votes += 1
    return votes

def testErr(n = 1000, p =46.0, numTrials=1000):
    results = []
    for t in range(numTrials):
        results.append(poll(n,p))
    print 'std = '+str((stdDev(results)/n)*100)+' %'
    results = pylab.array(results)/n
    pylab.hist(results)
    pylab.xlabel('Fraction of votes')
    pylab.ylabel('Number of Polls')

testErr()
pylab.show()
