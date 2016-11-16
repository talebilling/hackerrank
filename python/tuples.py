#!/bin/python3
# input:
# 2
# 1 2

n = int(input())
my_list = input().split(" ")

# for i in range(n):
#    my_list[i] = int(my_list[i])

# more advanced: my_list(map(int, my_list))

my_list = [int(item) for item in my_list]

hash_data = hash(tuple(my_list))
print(hash_data)
# output should be:  3713081631934410656
