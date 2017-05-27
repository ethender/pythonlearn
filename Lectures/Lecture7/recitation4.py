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
def rec_fib(n):
    '''
    A recursive function to find nth fibonacci
    n is an int >= 0
    '''
    #Base case: 0th fib number is 0 or 1
    if n==0 or n == 1:
        return n
    #Recursive case : nth fib number is sum of
    else:
        return rec_fib(n-1) + rec_fib(n-2)

print 'Recursive fibonacci'
print rec_fib(2)
print rec_fib(3)
print rec_fib(5)

##
## xrange() same as range() but more efiicient
##

