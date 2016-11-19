# input: abracadabra
#        5 k
# output: abrackdabra

'''
string = "abracadabra"
print(string)
mylist = list(string)
mylist[5] = "k"
print("".join(mylist))


new_string = string[:5] + "k" + string[6:]
print(new_string)
'''


def get_inputs_and_split():
    string = input()
    ind_and_char = input().split(" ")
    return string, ind_and_char


def str_to_int(ind_and_char):
    ind_and_char[0] = int(ind_and_char[0])
    return ind_and_char


def change_string(string, ind_and_char):
    string_list = list(string)
    index = 0
    char = 1
    string_list[ind_and_char[index]] = ind_and_char[char]
    new_string = "".join(string_list)
    return new_string


def main():
    string, ind_and_char = get_inputs_and_split()
    ind_and_char = str_to_int(ind_and_char)
    print(change_string(string, ind_and_char))

main()
