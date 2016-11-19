# input:
# ABCDCDc
# CDC
# output: 1


def main():
    string, substr = get_input()
    string_len, subs_len = find_string_lenghts(string, substr)
    print(find_substr_in_string(string_len, subs_len, string, substr))


def get_input():
    string = input()
    substr = input()
    return string, substr


def find_string_lenghts(string, substr):
    string_len = len(string)
    subs_len = len(substr)
    return string_len, subs_len


def find_substr_in_string(string_len, subs_len, string, substr):
    counter = 0
    loop_range = string_len - (subs_len - 1)
    for i in range(loop_range):
        if substr[0:subs_len] == string[i:(i + subs_len)]:
            counter += 1
    return counter


main()
