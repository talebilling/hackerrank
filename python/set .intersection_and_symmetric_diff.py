''' input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
'''


def main():
    eng_list, fre_list = get_input()
    print_intersection(eng_list, fre_list)
    print_symmetric_diff(eng_list, fre_list)
    return


def get_input():
    eng = int(input())
    eng_list = set(input().split())
    fre = int(input())
    fre_list = set(input().split())
    return eng_list, fre_list


def print_intersection(eng_list, fre_list):
    print(len(eng_list.intersection(fre_list)))


def print_symmetric_diff(eng_list, fre_list):
    print(len(eng_list.symmetric_difference(fre_list)))


main()
