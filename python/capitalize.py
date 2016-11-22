def get_input_and_split():
    return input().split(" ")


def string_capitalize(string):
    for i, item in enumerate(string):
        string[i] = item.capitalize()
    return string


def main():
    string = get_input_and_split()
    string = string_capitalize(string)
    print(string)
    print(" ".join(string))

main()
