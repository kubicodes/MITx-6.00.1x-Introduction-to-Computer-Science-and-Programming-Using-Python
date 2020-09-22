"""
Problem Set 2 
Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if a person only pays 
the minimum monthly payment required by the credit card company each month.
For each month, calculate statements on the monthly payment and remaining balance. 
At the end of 12 months, print out the remaining balance. Be sure to print out no more than two 
decimal digits of accuracy.

Notice that the input is provided by the coding environment on edX platform. So the variables
are not named locally. If you want to test the algorithm please make sure that you provide values in
variables wich are named like below in the algorithm.
"""

def calculateCreditCardBalance(balance, annualInterestRate, monthlyPaymentRate):
    unpaid_balance = balance - (balance*monthlyPaymentRate)
    
    for i in range(1,13):
        balance = round(unpaid_balance + (annualInterestRate/12.0) * unpaid_balance,2)
        unpaid_balance = balance - (balance*monthlyPaymentRate)
    
    return balance

print("Remaining balance: " + str(calculateCreditCardBalance(balance, annualInterestRate, monthlyPaymentRate)))

