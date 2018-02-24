##
##Lecture 7
##



##print(0.1)
##
##print repr(0.1)

##x = 0.0
##numIters = 100000
##for i in range(numIters):
##    x += 0.1
##print x #prints 10000.0, because print automatically rounds
##print repr(x)
##print 10.0*x == numIters
##
##
##
##def close(x,y,epsilon = 0.00001):
##    return abs(x-y) < epsilon
##
##if close(10.0*x,numIters):
##    print 'Good enough'



##
## checks is the palindrome
##
def isPal(x):
    """requires: x is a list
        returns true if the list is a palindrome: False otherwise"""
    assert type(x) == list
    temp = x[:] ## cloning
    temp.reverse()
    print 'temp =',temp
    print 'x = ',x
    if temp == x:
        return True
    else:
        return False


def silly(n):
    """requires n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the input are a palindrome; 'No' otherwise"""
    assert type(n) == int and n > 0
    result = []
    for i in range(n):
        elem = raw_input("Enter something: ")
        result.append(elem)
    if isPal(result):
        print 'Is a palindrome'
    else:
        print 'Is not a palindrome'
    
##def isPalTest():
##    l = [1,2]
##    result = isPal(l)
##    print 'should print False',result
##    l = [1,2,1]
##    result = isPal(l)
##    print 'should print True',result
##
##isPalTest()
