'''
changing the lower to upper and vica versa
input: HackerRank.com presents "Pythonist 2".
'''


def get_input():
    my_string = input()
    return my_string


# solution 1
def swap_one(string):
    new_string = string.swapcase()
    return new_string


# solution 2
def swap_two(string):
    return string.swapcase()


# solution 3
fvn = lambda string: string.swapcase()


my_string = get_input()
print(swap_one(my_string))
print(swap_two(my_string))
print(fvn(my_string))
