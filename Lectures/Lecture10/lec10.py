##
##
##
## Lec 10: Hashing and Classes
##
##
## 



##
##hash(i) 0->k
##
##
## list of list is called bucket
##
## hash is many to one
## collision -> linear rehashing to not collide
##
##


numBuckets = 47 #this is ugly. we will see a better way soon

def create():
    global numBuckets
    hSet = []
    for i in range(numBuckets):
        hSet.append([])
    return hSet

def hashElem(e):
    global numBuckets
    return e%numBuckets

def insert(hSet, i):
    global numBuckets
    hSet[hashElem(i)].append(i)

def remove(hSet, i):
    newBucket = []
    for j in hSet[hashElem(i)]:
        if j != i:
            newBucket.append(j)
    hSet[hashElem(i)] = newBucket


def member(hSet, i):
    return i in hSet[hashElem(i)]

numBuckets = 47
def test1():
    s = create()
    for i in range(40):
        insert(s, i)
    insert(s,325)
    insert(s,325)
    insert(s, 987654321)
    print s
    print member(s,325)
    remove(s,325)
    print member(s,325)
    print member(s,987654321)


def hashELem(e):
    global numBuckets
    if type(e) == int:
        val = e
    if type(e) == str:
        #convert e to int
        val = 0
        shift = 0
        for c in e:
            val = val + shift*ord(c)
            shift += 1
    return val%numBuckets


def test2():
    d = create()
    str = ['ab','ba', '32s', 'big dog', 'small bird']
    for s in strs:
        insert(d,s)
    for i in range(40):
        insert(d,i)
    print d
    print member(d, 'samll bird')
    print member(d, 'big dog')


##
##
## exceptions
##
##unhandled exceptions
##
##
##try:    
##  code
##except:
##  code   
##


def readVal(valType, requestMsg, errorMsg):
    numTries = 0
    while numTries < 4:
        val = raw_input(requestMsg)
        try:
           val = valType(val)
           return val
        except ValueError:
             print(errorMsg)
            numTries += 1
    raise TypeError('Num tries exceeded')
    
##print readVal(int, 'Enter int:' , 'Not and int.')

try:
    readVal(int,'Enter int: ','Not an int.')
except TypeError, s:
    print s


##
##
## Class
##
## Module - collection related functions
##  import math
##      math.log
##          |
##          dot notation uses disambiguate
##
##  class is a collection of data and functions
##      function is for operate data 
##
##
##
##  Objected - oriented programming
##    L.append(e) ->  Associate attributes with objects
##
##
##  Message passing metaphor
##
##  method is  a function associated with an object
##
##    
