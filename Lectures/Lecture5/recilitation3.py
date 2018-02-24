
#R03.py


example = int(raw_input("Example number"))


#Example 1 : Review of Tuples

if example == 1:
    # Tuples may have any type of element in them -
    # strings , ints, floats , other tuples or other lists

    tupA = (1,"apple",6.00)
    tupB = (tupA,"MIT",[4,5])

    print "tupA is", tupA, "with length ",len(tupA)
    print "tupB is",tupB, "with length",len(tupB)

    print "\nIndexing operations. "
    print "tup[0] is : ",tupA[0]
    print "tupA[2] is: ",tupA[2]
    #print "tupA[3] is: ",tupA[3] #error -why?
    print "tupB[0][1] is: ",tupB[0][1]
    print "tupB[-1] is: ",tupB[-1]



    print "\nSlicing operations"
    print "tupA[0:1] is:",tupA[0:2]
    print "tupA[0:100] is:",tupA[0:100]
    print "tup[0:2] is: ",tupA[0:2]
    print "tupA[:2] is: ",tupA[:2]
    print "tupA[1:] is: ",tupA[1:]
    print "tupA[:] is: ",tupA[:]
    print "tupB[-1:-3] is: ",tupB[-1:-3]


    #Iteration through tuple
    print "\nIteration through tupB: "
    for item in tupB:
        print item," is of type ",type(item)


    #this is equivalent to
    print "\nIteration through tupB: "
    for i in range(len(tupB)):
        print tupB[i], 'is of type ',type(tupB[i])

    #extend operations for tuples
        print tupA+tupB

elif example == 2:

    emptyList1 = [0]*10 # creates 10 0 values
    emptyList2 = [[]]*10 # create 10 empty values


    #Iterations through list
    for item in emptyList1:
        print item,'is of type',type(item)

    #access inner list
    print "\n Access inner list"
    L = [['mit','stanford'],['harvard','uop'],0]
    print 'In List ',L
    print 'L[0][1] is ',L[0][1] #prints stanford

    print "\n Matrix"
    # create a matrix
    M = [[0,1],[1,2],[2,3],[3,4]]
    print M

elif example == 3:
    LA = [6.00, "MIT",600,600]
    LA.append('Harvard')
    print LA


    LA.append(['Yale','Stanford'])
    print LA

    LA.pop() # pop off the last element
    print LA
    LA.pop(0) # pop off element at index 0


    LA.extend(['YALE','Stanford'])
    print LA
    LA.remove(600)
    print LA
               

elif example == 4:

    staff = {
            'ceo': 'ceo@hawks.org',
            'hacker':'ethender@hawks.org'
        }


    print len(staff)

    staff['ceo'] = 'aryan@hawks.org'
    staff['admin'] = 'admin@hawks.org'

        
    if 'ceo' in staff:
        print 'hello arya'

    if 'aryaethender' not in staff:
        staff['aryaethender'] = 'aryaethender@hawks.org'

    print staff
    staff.keys().sort()
    print staff


    del staff['aryaethender']
    print staff


    for name, email in staff.items():
        print 'name: ',name,' can be contacted at: ',email

    
elif example == 5:

    def factorial(a):
        if a == 0:
            return 1
        else:
            return a * factorial(a-1)



    print factorial(0)
    print factorial(5)


elif example == 6:
    def hanoi(n,s,t,b):
        assert n > 0
        if n == 1:
            print 'move  ',s,' to ',t
        else:
            hanoi(n-1,s,b,t)
            hanoi(1,s,t,b)
            hanoi(n-1,b,t,s)

    for i in range(1,5):
        print "new hanoi example hanoi(",i,"source,target,buffer)"
        print '----------------------'
        hanoi(i,"Source","Target","Buffer")
