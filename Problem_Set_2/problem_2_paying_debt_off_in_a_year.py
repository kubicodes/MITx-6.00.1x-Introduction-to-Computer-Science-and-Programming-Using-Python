"""
Problem Set 2 
Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed in order pay off 
a credit card balance within 12 months. By a fixed monthly payment, 
we mean a single number which does not change each month, but instead is 
a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.


Notice that the input is provided by the coding environment on edX platform. So the variables
are not named locally. If you want to test the algorithm please make sure that you provide values in
variables wich are named like below in the algorithm.
"""

def defineMonthlyPayment(balance, annualInterestRate):
    monthly_payment = 0
    current_balance = balance
    monthly_interest = annualInterestRate/12
        
    while balance > 0:
        for i in range(12):
            balance = balance - monthly_payment + ((balance - monthly_payment)*monthly_interest)
            
        if balance > 0:
            monthly_payment += 10
            balance = current_balance
        elif balance <=0:
            break
    return monthly_payment
  
print('Lowest Payment:', defineMonthlyPayment(balance, annualInterestRate))