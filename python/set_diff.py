''' Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
'''


def main():
    a, b = get_input()
    print(set_difference(a, b))


def get_input():
    a_len = int(input())
    a = set(input().split())
    b_len = int(input())
    b = set(input().split())
    return a, b


def set_difference(a, b):
    student_set_diff = a.difference(b)
    lenght = len(student_set_diff)
    return lenght

main()
