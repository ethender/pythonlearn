
## Write a program to calculate the credit card balance after one year if a person only pays the
## minimum monthly payment required by the credit card company each month.





#
## Calculates the minimummonthly amount
#
def minimumMonthlyPayment(monthlyInterest, amount):
    return monthlyInterest * amount


#
## Calculates the interest paid
def calculateInterestPaid(interest, balance):
    return ((interest/12.0)*(balance))


def calculatePrincipalPaid(minimumAmount, interestPaid):
    return (minimumAmount - interestPaid)

#
## Three Floating Numbers
#

creditBalance = float(raw_input('Enter the outstanding balance on your credit card: '))
creditCardInterest = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
creditCardMonthlyRate = float(raw_input('Entere the minimum monthly payment rate as a decimal: '))



## storing minimum amount and paid amount
minimumAmount = (0,creditBalance)
paidAmount = 0


## for loop
for i in range(1,13):
    print 'Month :',i
    amount = minimumAmount[-1]
    minimumPay = minimumMonthlyPayment(creditCardMonthlyRate,amount)
    interestPaid = calculateInterestPaid(creditCardInterest,amount)
    principaid = calculatePrincipalPaid(minimumPay, interestPaid)
    paidAmount += minimumPay
    remainAmount = amount - principaid
    #minimumAmount = minimumAmount + remainAmount

    minimumAmount = list(minimumAmount)
    minimumAmount.insert(len(minimumAmount),remainAmount)
    minimumAmount = tuple(minimumAmount)

    print 'Minimum monthly payment: $',round(minimumPay,2)
    print 'Principle paid: $',round(principaid,2)
    print 'Remaining balance: $',round(remainAmount,2)


## printing result
print 'RESULT'
print 'Total amount paid: $',round(paidAmount,2)
print 'Remaining balance: $',round(minimumAmount[-1],2)
