"""
Problem Set 1
Problem 2

Assume s is a string of lower case characters. Write a program that prints the number 
of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', 
then your program should print: Number of times bob occurs is: 2

Notice that the input is provided by the coding environment on edX platform. So the variables
are not named locally. If you want to test the algorithm please make sure that you provide values in
variables wich are named like below in the algorithm.
"""

counter = 0

for i in range(0,len(s)):
    if s[i] == 'b' and s[(i+1):(i+3)] == 'ob':
        counter += 1

print("Number of times bob occurs is: " + str(counter))  