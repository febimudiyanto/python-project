balance = float(input("balance = "))
annualInterestRate = float(input("Interest Rate = "))


# Paste your code into this box
'''
Problem Set 2
( Problem 2 - Paying Debt off in a Year)

balance = the outstanding balance on the credit card
annualInterestRate = annual interest rate as a decimal

'''

def cek_bulan(fixedMonthlyPayment,balance):
    '''
    fixedMonthlyPayment = Fixed payment for all months
    balance = the outstanding balance on the credit card
    
    return boolean (true/false)

    '''
    
    bulan = 0
    while balance > 0 and bulan <= 12 :
        balance = (balance - fixedMonthlyPayment) * (monthlyInterestRate + 1)
        bulan += 1
    
    return bulan <= 12



monthlyInterestRate = (annualInterestRate)/12.0
lowestMontlyPayment = 10

while not cek_bulan(lowestMontlyPayment,balance):
    lowestMontlyPayment += 10

print("Lowest Payment:",lowestMontlyPayment)


