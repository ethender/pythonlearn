##                           Lecture - 2

##print type(3)


## Assignment Operator
##x =  3
##x = x*x
##print x



##
##y =  float(raw_input('Enter an integer: '))
##print y
##print type(y)
##    
##x=  raw_input('Enter an integer: ')
##print x
##print type(x)


##x = int(raw_input('Enter an integer: '))
##if  x%2 == 0:
##        print 'Even'
##else :
##        print 'Odd'
##        if x%3 != 0 :
##            print 'And not divisible by 3'

## Find the cube root of a perfect cube
x = int(raw_input('Enter an  integer: '))
ans = 0
while ans*ans*ans < abs(x):
    ans =  ans + 1
    #print 'current guess =',ans
if ans*ans*ans != abs(x):
    print x, 'is not a perfect cube'
else:
    if x < 0:
        ans = -ans
    print 'Cube root of' +  str(x) +' is '+ str(ans)
    
