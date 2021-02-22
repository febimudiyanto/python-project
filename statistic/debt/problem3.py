'''
Problem Set 2
( Problem 3 - Paying Debt off in a Year)

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
        
    return bulan,balance


monthlyInterestRate = (annualInterestRate)/12.0
lowestMontlyPayment = 10

while cek_bulan(lowestMontlyPayment,balance)[0] > 12:
    lowestMontlyPayment += 10



cek = lowestMontlyPayment
lowestMontlyPayment -= 10
while lowestMontlyPayment <= cek:
    if cek_bulan(lowestMontlyPayment,balance)[0] == 12:
        print("Lowest Payment:",round(lowestMontlyPayment,2))
        break
    lowestMontlyPayment += 0.01
    


