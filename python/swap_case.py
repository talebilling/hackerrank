'''
changing the lower to upper and vica versa
'''
my_string = input()

# solution 1
new_string = my_string.swapcase()
print(new_string)


# solution 2
def swap(string):
    return string.swapcase()
print(swap(my_string))


# solution 3
fvn = lambda string: string.swapcase()
print(fvn(my_string))
