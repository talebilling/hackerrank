''' input: 
3 2 - lenghts
1 5 3 - nums of lists
3 1 - set numbers - gives +1
5 7 - set numbers - gives -1
3 2
1 5 3
3 1
5 7
'''


def main():
    my_list, a, b = get_input()
    print_happiness_counter(my_list, a, b)
    return


def get_input():
    lenght_list = input().split()
    my_list = input().split()
    a = set(input().split())
    b = set(input().split())
    return my_list, a, b


def print_happiness_counter(my_list, a, b):
    happiness_counter = 0
    for item in my_list:
        if item in a:
            happiness_counter += 1
        elif item in b:
            happiness_counter -= 1
    print(happiness_counter)

main()
