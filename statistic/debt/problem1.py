balance = float(input("balance = "))
annualInterestRate = float(input("Interest Rate = "))
monthlyPaymentRate = float(input(" Minimum monthly payment rate (as a decimal ) = "))

'''
Problem Set 2
( Problem 1 - Paying Debt off in a Year)

balance = the outstanding balance on the credit card
annualInterestRate = annual interest rate as a decimal
monthlyPaymentRate = minimum monthly payment rate as a decimal
'''

monthlyInterestRate = (annualInterestRate)/12.0

for _ in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

print("Remaining balance:",round(balance,2))
