"""
Problem Set 1
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print:
    Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print:
    Longest substring in alphabetical order is: abc

Notice that the input is provided by the coding environment on edX platform. So the variables
are not named locally. If you want to test the algorithm please make sure that you provide values in
variables wich are named like below in the algorithm.
"""

previous_letter = ""
current_string = ""
longest_string = ""

for letter in s:
    if previous_letter <= letter:
        current_string += letter
        if len(current_string) > len(longest_string):
            longest_string = current_string
    else:
        current_string = letter
    previous_letter = letter
print('Longest substring in alphabetical order is: ' + longest_string )