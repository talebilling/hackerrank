''' Input:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
    output 4
'''


def main():
    my_set, command_num = get_input()

    for i in range(command_num):
        command = get_command()

        if command[0] == "pop":
            my_set.pop()
        elif command[0] == "discard":
            num = int(command[1])
            my_set.discard(num)
        elif command[0] == "remove":
            num = int(command[1])
            my_set.remove(num)
    print_set(my_set)


def get_input():
    my_set_len = int(input())
    my_set = set(map(int, input().split()))
    command_num = int(input())
    return my_set, command_num


def get_command():
    return input().split()


def print_set(my_set):
    print(sum(my_set))


main()
