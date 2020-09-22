"""
Problem Set 2 
Problem 3 - Using Bisection Search to Make the Program Faster

Write a program that uses these bounds and bisection search to find the smallest 
monthly payment to the cent (no more multiples of $10) such that we can pay off
the debt within a year. Try it out with large inputs, and notice how fast it is. 
Produce the same return value as you did in Problem 2.


Notice that the input is provided by the coding environment on edX platform. So the variables
are not named locally. If you want to test the algorithm please make sure that you provide values in
variables wich are named like below in the algorithm.
"""


init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))
