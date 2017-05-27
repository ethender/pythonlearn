###finding square  root 
##x = 0.5
##epsilon = 0.01
##low = 0.0
##high =  max(x, 1.0)
##ans = (high+low)/2.0
##
##while  abs(ans**2) >= epsilon and (ans <= x):
##    print 'ans = ', ans, 'low = ', low, 'high = ', high
##    if ans**2 < x:
##        low = ans
##    else:
##        high = ans
##    ans = (high+low)/2.0
##    print ans, 'is close to square root of', x


##
##def withinEpsilon(x,y,epsilon):
##    ##***x,y, epsilon floats. epsilon >0.0
####            returns True if x is within epsilon of y***
##            return abs(x - y) <= epsilon
##
##print withinEpsilon(2,25,5)

##def f(x):
##    x = x+1
##    print 'x=',x
##    return x
##
##x = 3
##z= f(x)
##print 'z = ',z
##print 'x = ',x


##def f1(x):
##    def g():
##            x = 'abc'
##            assert False ##breaks the program if false -> see on the stack viewer on console
##    x = x + 1
##    print 'x = ',x
##    g()
##    return x
##
##x =3
##x = f1(x)


##
## Test this name function in console
## >>> name('ethender')
## >>> Hello ethender // this will print
##

##
##def name(e):
##    print 'Hello ',e



##sumDigits = 0
##for c in str(1952):
##    sumDigits += int(c)
##print sumDigits



####
####Slicing
##
##s = 'abc'
##print s[0]
##print s[0:1]


x = 100
divisors = ()
print divisors
for i in range(1,x):
    if x%i == 0:
        divisors = divisors + (i,)
        print divisors

print divisors
print divisors[0] + divisors[1]
print divisors[2:4]
