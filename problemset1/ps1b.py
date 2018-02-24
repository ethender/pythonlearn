

##
## Minimum Monthly Payment
##

def minimumMonthlyPayment(monthlyInterests, amount):
    return monthlyInterests * amount



##
## monthly interest
##
def monthlyInterestRate(annualInterestRate):
    return annualInterestRate/12.0


##
##  update balance 
##
def updateMonthlyBalance(previousBalance, monthlyInterestRates, minimumMonthPayment):
        interest  = (1+monthlyInterestRates)
        amount = previousBalance * interest
        return amount - minimumMonthPayment

##
##  checking paying money is sufficient to clear debit in one year 
##    
def checkIsSufficientMoney(previousBalance,monthlyInterestRates,amount):
    result = False
    for i in range(1,13):
        previousBalance = updateMonthlyBalance(previousBalance,monthlyInterestRates,amount)
        if previousBalance < 0:
            result = True
    return result

##
##  if sufficient amount we are paying checking how many months to clear
##
def getMonths(previousBalance,monthlyInterestRates,amount):
    result = 0
    for i in range(1,13):
        previousBalance = updateMonthlyBalance(previousBalance,monthlyInterestRates,amount)
        if previousBalance < 0:
            result = i
    return result

##
##  Final Balance
##
def getAmountAfterYear(previousBalance,monthlyInterestRates,amount,month):
    for i in range(1,month):
        previousBalance = updateMonthlyBalance(previousBalance,monthlyInterestRates,amount)
    return previousBalance


##
##pre-requistes
##
outstandingAmount = float(raw_input("Enter the outstanding balance on your credit card: "))
annualInterest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
monthlyInterest = monthlyInterestRate(annualInterest)

temp = outstandingAmount

##main program
i = 1
iPay = 10
while True:
    if checkIsSufficientMoney(temp,monthlyInterest,(iPay*i)):
        print 'RESULT'
        month = getMonths(temp,monthlyInterest,(iPay*i))
        print 'Monthly payment to pay off debit in 1 year: '+str(iPay*i)
        print 'Number of months needed: '+str(month)
        balance = round(getAmountAfterYear(temp,monthlyInterest,(iPay*i),month),2)
        print 'Balance: '+str(balance)
        break
    else:
        i += 1



