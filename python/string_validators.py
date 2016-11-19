# input: qA2
'''
Output Format
print True if  has any alphanumeric characters. Otherwise, print False. 
print True if  has any alphabetical characters. Otherwise, print False. 
print True if  has any digits. Otherwise, print False. 
print True if  has any lowercase characters. Otherwise, print False. 
print True if  has any uppercase characters. Otherwise, print False.
'''


def check_input_and_print_flag(given_str):
    print(any(i.isalnum() for i in given_str))
    print(any(i.isalpha() for i in given_str))
    print(any(i.isdigit() for i in given_str))
    print(any(i.islower() for i in given_str))
    print(any(i.isupper() for i in given_str))


def get_input():
    return input()


def main():
    given_str = get_input()
    check_input_and_print_flag(given_str)

main()
