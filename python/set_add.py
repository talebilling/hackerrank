'''
Sample Input:
7
UK
China
USA
France
New Zealand
UK
France
Output the total number of distinct country stamps on a single line.
'''


def main():
    stamps_set = get_input()
    print_lenght(stamps_set)


def get_input():
    n = int(input())
    stamps_set = set()
    for i in range(n):
        string = input()
        stamps_set.add(string)
    return stamps_set


def print_lenght(stamps_set):
    lenght = len(stamps_set)
    print(lenght)

main()
