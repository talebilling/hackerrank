#!/bin/python3


# this print a list of sequence
def print_list(a):
    b = []
    for i in range(a + 1):
        b.append(i)
    return b


# this print the sequence as strings
def print_sequence(a):
    return (''.join(str(a) for a in range(1, a + 1)))


def get_input():
    return int(input())


def main():
    a = get_input()
    print(print_list(a))
    print(print_sequence(a))

main()
