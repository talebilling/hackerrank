# input:
# 10
# 161 182 161 154 176 170 167 171 170 174


def main():
    num_list = get_input_make_list()
    num_list = make_int_in_input_list(num_list)
    num_set = make_set_from_list(num_list)
    average = calc_average(num_set)
    print(average)


def get_input_make_list():
    num = int(input())
    num_list = input().split(" ")
    return num_list


def make_int_in_input_list(num_list):
    # convert str-s to int with map(func, iterables)
    num_list = list(map(int, num_list))
    return num_list


def make_set_from_list(num_list):
    num_set = set(num_list)
    return num_set


def calc_average(num_set):
    average = sum(num_set) / len(num_set)
    return average

main()


'''
num = int(input())
num_list = input().split()

for i, item in enumerate(num_list):
    num_list[i] = int(item)
    
num_set = set(num_list)
average = sum(num_set) / len(num_set)
print(average)
'''
