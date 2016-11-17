'''
Task 
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''

import sys
# input a number


def get_input():
    n = int(input().strip())
    return n


def check_given_number(n):
    if n % 2 != 0:
        print(weird)
    if n % 2 == 0:
        if n in range(2, 6) or 21 < n:
            print(notwierd)
        elif n in range(6, 22):
            print(weird)


weird = "Weird"
notwierd = "Not Weird"
n = get_input()
check_given_number(n)
