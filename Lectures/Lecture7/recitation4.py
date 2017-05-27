##
##
##

##
## Multiplication (pretend no * operator available)
##

##def rec_mult(m,n):
##    #Base case (only occur if call the function)
##    if n == 0:
##        return 0
##    elif n >= 1:
##        return m + rec_mult(m,n-1)
##    elif n <= -1:
##        return -m + rec_mult(m,n+1)
##
####Test 1 Remember test cases should always tet
#### inputs, and be teste that you know the correct answer
##
##print 'Recursive multiplication tests:'
##print rec_mult(8,0)#0
##print rec_mult(3,4) # 12
##print rec_mult(-3,4) #-12
##
##


##
## Fibonacci
##
##def rec_fib(n):
##    '''
##    A recursive function to find nth fibonacci
##    n is an int >= 0
##    '''
##    #Base case: 0th fib number is 0 or 1
##    if n==0 or n == 1:
##        return n
##    #Recursive case : nth fib number is sum of
##    else:
##        return rec_fib(n-1) + rec_fib(n-2)
##
##print 'Recursive fibonacci'
##print rec_fib(2)
##print rec_fib(3)
##print rec_fib(5)

##
## xrange() same as range() but more efiicient
##

##
##square root using bisection search
##

##def rec_bisection_sqrt(x,epsilon=0.01,low=None,high=None):
##    '''
##    Performs a recursive bisection search to find the square root of x, within episilon
##    '''
##    if low == None:
##        low =0.0
##    if high == None:
##        high = x
##    midpoint = (low+high)/2.0
##
##    if abs(midpoint**2-x) < epsilon or midpoint > x:
##        return midpoint
##    else:
##        if midpoint**2 < x:
##            return rec_bisection_sqrt(x,epsilon,midpoint,high)
##        else:
##            return rec_bisection_sqrt(x,epsilon,low,midpoint)
##
##
##print rec_bisection_sqrt(25)



##
##
##
##      Floting Numbers
##
##
##

##ten_hundredths = 10/100.0
##one_hundredths = 1/100.0
##nine_hundredths = 0/100.0
##if ten_hundredths == (one_hundredths+nine_hundredths):
##    print 'Yes, (10/100.0) equals (1/100.0 + 9/100.0)'
##else:
##    print 'No, (10/100.0) equals (1/100.0 + 9/100.0)'
##    print '10/100.0 is:',ten_hundredths,'... which Python represents ',repr(one_hundredths+nine_hundredths)
##    print '10/100.0 is:',(one_hundredths+nine_hundredths),'... which Python represents ',\
##          repr(one_hundredths+nine_hundredths)
##
##
##
##nine_hundredths_plus_one_hundredth = nine_hundredths + one_hundredth
##nine_hundredths_plus_one_hundredth -= nine_hundredths
##print '9/100.0 + 1/100.0 = 1/100.0 == 9/100.0 : ',\
##    nine_hundredths_plus_one_hundredth == nine_hundredths



##
##
##
##  pseudo code
##
##Means : divide the problem and plan how to write the code
##

