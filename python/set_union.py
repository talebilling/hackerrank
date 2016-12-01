'''
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
'''


def main():
    a, b = get_input()
    student_set = make_union_a_b(a, b)
    print_set_lenght(student_set)


def get_input():
    a_len = int(input())
    a = input().split()
    b_len = int(input())
    b = input().split()
    return a, b


def make_union_a_b(a, b):
    student_set = set()
    for item in a:
        student_set.add(item)
    for item in b:
        student_set.add(item)
    return student_set


def print_set_lenght(student_set):
    print(len(student_set))

main()
