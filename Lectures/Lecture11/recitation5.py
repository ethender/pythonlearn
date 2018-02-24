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

##print f('mat')
##print f('math')


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

def set_name(person, name):
    person['name'] = name
    
def get_age(person):
    return person['age']

def set_age(person,age):
    person['age'] =  age

def get_height(person):
    return person['height']

def set_height(person, height):
    person['height'] = height

def get_weight(person):
    return person['weight']

def set_weight(person, weight):
    person['weight'] = weight

def print_person(person):
    print 'Name: ',get_name(person), ', Age: ',get_age(person)

mitch = make_person('Mitch', 32, 70, 200)
sarina = make_person('Sarina', 25, 65, 130)

##print_person(mitch)


##print type(mitch)
not_a_person = {'RandomJunk':'Junk','Junk':'RndomJunk'}
##print_person(not_a_person)



def people_equal(person1, person2):
    return get_name(person1) == get_name(person2)

##print people_equal(sarina, mitch)



class Person(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # this type is called a accessor
    def get_name(self):
        return self.name
    # this type is called a mutator
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height

    def get_weight(self):
        return self.weight

    def set_weight(self):
        self.weight = weight

    # underbar methods have special significance in python
    def __str__(self):
        return 'Name: '+self.name+', Age: '+str(self.age)
    
    def __eq__(self, other):
        return self.name == other.name


mitch = Person('Mitch',32, 70, 200)
sarina = Person('Sarina', 25, 65, 130)

##print mitch
##mitch.set_age(25)
##print mitch
##print type(mitch)
##print mitch == sarina
##dir(object)

##
##print mitch.get_age()
##print Person.get_age(mitch)



class Shape(object):
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * self.side1 + 2 * self.side2
    def __str(self):
        return 'Rectangle('+str(self.side1)+","+str(self.side2)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2.0 * 3.14159 * self.radius

    def __str(self):
        return 'Circle('+str(self.radius)+')'

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def __str__(self):
        return 'Square( '+str(self.side)+')'

a = Shape()
##print a.area()

r = Rectangle(2,8)
sq = Square(4)
c = Circle(10)

print 'Recatngle area: ',r.area()
print 'Square area: ', sq.area()
print 'Circle area: ',c.area()

    
    

