#!/bin/python3
'''
Task 
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
INPUT:
insert 0 5
insert 1 10
insert 0 6
remove 6
append 9
append 1
'''
number_of_commands = int(input())
my_list = []

for i in range(number_of_commands):
    inp = (input())
    input_list = inp.split(" ")
    command = 0

    if input_list[command] == "insert":
        my_list.insert(int(input_list[1]), int(input_list[2]))
    elif input_list[command] == "remove":
        my_list.remove(int(input_list[1]))
    elif input_list[command] == "append":
        my_list.append(int(input_list[1]))
    elif input_list[command] == "sort":
        my_list.sort()
    elif input_list[command] == "pop":
        my_list.pop()
    elif input_list[command] == "reverse":
        my_list.reverse()
    elif input_list[command] == "print":
        print(my_list)
