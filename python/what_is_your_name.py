#!/bin/python3
# input 2 lines: first and second name


def print_hello(first_name, second_name):
    print("Hello {0} {1}! You just delved into python.".format(first_name, second_name))


def get_input():
    first_name = input()
    second_name = input()
    return first_name, second_name


def main():
    first_name, second_name = get_input()
    print_hello(first_name, second_name)
    return

main()
