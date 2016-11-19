#!/bin/python3
# input: this is a string


def split_input():
    string = input().split(" ")
    return string


def join_strings(string):
    new_string = "-".join(string)
    return new_string


def main():
    string = split_input()
    print(join_strings(string))
    return

main()
