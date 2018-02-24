
"""
    computes the polynomials """


poly = (0.0,0.0,5.0,9.3,7.0)
x = -13



def evaluate_poly(polynomial,x):
    total = 0.0
    power = 0
    for i in polynomial:
       total += (i)*(x**power)
       power += 1

    return total

print poly
print x
print evaluate_poly(poly,x)


