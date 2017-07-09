##
##
## Recitation 5: Quiz 1 Answers and Object-Oriented Programming
##
##
##
##



##T = (0.1, 0.1)
##x = 0.0
##for i in range(len(T)):
##    for j in T:
##        x += i + j
##        print x
##print i


##
## Double Recursion
##
def f(s):
    if len(s) <= 1:
        return s
    return f(f(s[1:]))+ s[0]

print f('mat')
print f('math')


##
## question 4
##
def findAll(wordlist, lStr):
    retWords = []
    sortedStr = "".join(sorted(lStr))
    for word in wordList:
        soretedWord = "".join(sorted(word))
        if sortedLastr == sortedWord:
            retWords.append(word)
    return retWords

##
## Question: 5
##
##
def addVector(v1, v2):
    """ex: [[4,5],[1,2,3]] returns [5,6,3] , [[],[]] -> [] """
    if len(v1) > len(v2):
        result = v1[:]
        other = v2
    else:
        result = v2[:]
        other = v1
    for i in range(len(other)):
        result[i] += other[i]
    return result


##
##  class                               type
##   methods                            int
##                                      float
##                                      dicts
##
##  attributes
##  
##


def make_person(name,age, height, weight):
    person = {}
    person['name'] = name
    person['age'] = age
    person['height'] = height
    person['weight'] = weight
    return person

def get_name(person):
    return person['name']

def get_age(person):
    return person['age']

def get_height(person):
    return person['height']

def get_weight(person):
    return person['weight']

def print_person(person):
    return 'Name: ',get_name(person)

