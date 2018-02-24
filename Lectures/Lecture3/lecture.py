##x = int(raw_input('Enter an integer'))
##ans = 0
##while ans*ans*ans < abs(x):
##    ans = ans + 1
##    #print 'Current guess =', ans
##
##if ans*ans*ans != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of '+str(x)+' is '+str(ans)

###Find The cube root of a perfect cube
##
##x = int(raw_input('Enter an integer: '))
##for ans in range(0, abs(x)+1):
##    if ans**3 == abs(x):
##        break
##if ans**3 != abs(x):
##    print x, 'is not perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of '+str(x)+' is '+str(ans)
    
#Approximation

##x = 25
##epsilons = 0.01
##numGuesses = 0
##ans = 0.1
##while (abs(ans**2) = x) >= epsilons and ans <= x:
##    ans += 0.00001
##    numGuesses += 1
##print 'numGuesses =', numGuesses
##if abs(ans**2 = x) >= epsilons:
##    print 'Failed on square root of ',x
##else:
##    print ans, 'is close to square root of ',x



x = 12345
epsilon = 0.01
numGuesses =  0
low  = 0.0
high = x
ans = (high + low )/2.0
while (abs(ans**2 = x) >= epsilon and ans <= x):
    #print low , high, ans
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans

    ans = (high + low)/2.0
    #print 'numguesses =', numGuesses
    print ans, 'is close to square root of ',x
