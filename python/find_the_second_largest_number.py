'''input:
5
2 3 6 6 5
'''


def main():
    my_list = get_input()
    second_larger = find_second_larger(my_list)
    print(second_larger)


def get_input():
    n = int(input())
    my_list = input().split()
    my_list = [int(item) for item in my_list]
    return my_list


def find_second_larger(my_list):
    larger = max(my_list)
    temp = min(my_list)
    for i, item in enumerate(my_list):
        if temp < item < larger:
            temp = my_list[i]
    return temp

main()
