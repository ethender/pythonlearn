

##minimum monthly payment
def minimumMonthlyPayment(monthlyPaymentRate, balance):
    return (monthlyPaymentRate*balance)


##interest paid 
def interestPaid(annualInterest,balance):
    monthlyInterest = annualInterest/12.0
    return (monthlyInterest*balance)

## principal amount
def prinicipal(minimum, interest):
    return (minimum - interest)

## remaining balance
def remainingBalance(balance , principal):
    return (balance - principal)

## calculate whole for a year
def calculate(outstanding, annual, minimumMonthlyRate):
    balance = outstanding
    totalPP = 0
    for i in range(1,13) :
        ma = minimumMonthlyPayment(minimumMonthlyRate, balance)
        ip = interestPaid(annual,balance)
        pp = prinicipal(ma,ip)
        balance = remainingBalance(balance, pp)
        print 'Month: '+str(i)
        print 'Minimum monthly payment: $'+str(round(ma,2))
        print 'Principle paid: $'+str(round(pp,2))
        print 'Remianing balance: $'+str(round(balance,2))
        totalPP += pp
    print 'Total amount paid: $'+str(round(totalPP,2))
    print 'Remaining balance: $'+str(round(balance,2))
        
## main
def main():
    outstandingBalance = float(raw_input('Enter the outstanding balance on your credit card: '))
    annualInterest = float(raw_input('Enter an annual credit card interest rate as a decimal: '))
    minimumMonthly = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))
    calculate(outstandingBalance,annualInterest,minimumMonthly)


main()
    
