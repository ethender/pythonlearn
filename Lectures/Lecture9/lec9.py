##
##
##  Lecture 9: Memory and Search Methods
##
##
##

##
##Binary sort will work only list is sorted
##


##
##amortized complexity
##


##
## if we plan on k searches
## 0(sort(L)) + k * log(len(L)) < k * len(L)
##

##
##  selection sort
##
##def selSort(L):
##    for i in range(len(L) - 1):
##        minIndex = i
##        minVal = L[i]
##        j = i + 1
##        while j < len(L):
##            if minVal > L[j]:
##                minIndex = j
##                minVal = L[j]
##            j += 1
##        temp = L[i]
##        L[i] = L[minIndex]
##        L[minIndex] = temp
##        print 'Partially sorted list =',L
##
##
##L = [35,4,5,1,3]
##selSort(L)
##print 'Sorted List =',L


##
##Divide and conquer
##
##1. Threshold input size, no, smallest problem
##2. How Many instances at each division
##3. combine sub-solutions


def merge(left, right, lt):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if lt(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def sort(L, lt = lambda x,y:x<y):
    if len(L)<2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = sort(L[:middle], lt)
        right = sort(L[middle:],lt)
        print 'About to merge ',left, ' and ',right
        return  merge(left,right,lt)

##L = [35,1,7,4,2,9,10]
##newL = sort(L)
##print 'sorted list = ',newL
##L = [1.0,2.25,24.5,12.0,2.0,23.0,19.125,1.0]
##newL = sort(L,float.__lt__)
##print 'Sorted list =',newL


def lastNameFirstName(name1, name2):
    import string
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')
    if name1[1] != name2[1]:
        return name1[1] < name2[1]
    else:
        return name1[0] < name2[0]

def firstNameLastName(name1,name2):
    import string
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')
    if name1[1] != name2[1]:
        return name1[0] < name2[0]
    else:
        return name1[1] < name2[1]


L = ['John Guttag','Tom Brady' , 'chancellor grimson']
newL = sort(L,lastNameFirstName)
print 'sorted list =',newL
newL = sort(L,firstNameLastName)
print 'sorted list =',newL
