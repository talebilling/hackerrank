'''
input:
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
output: 38
'''


def main():
    a_len = int(input())
    a = set(input().split())
    a = change_set(a)
    make_list_and_print(a)


def change_set(a):
    comm_number = int(input())
    for i in range(comm_number):
        command, n = get_inputs()
        if command == "intersection_update":
            a.intersection_update(n)
        if command == "update":
            a.update(n)
        if command == "symmetric_difference_update":
            a.symmetric_difference_update(n)
        if command == "difference_update":
            a.difference_update(n)
    return a


def get_inputs():
    command_list = input().split()
    command = command_list[0]
    n = set(input().split())
    return command, n


def make_list_and_print(a):
    a = list(a)
    for ind, item in enumerate(a):
        a[ind] = int(item)
    print(sum(a))

main()
