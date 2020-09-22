"""
Problem Set 1
Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
your program should print: Number of vowels: 5

Notice that the input is provided by the coding environment on edX platform. So the variables
are not named locally. If you want to test the algorithm please make sure that you provide values in
variables wich are named like below in the algorithm.
"""

counter = 0

for letter in s:
    
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        counter += 1

print ("Number of vowels: " + str(counter))