def get_input():
    n = int(input())
    return n


def making_lists(n, decimal, octal, hexadecimal, binary):
    for num in range(1, n + 1):
        decimal.append(str(num))
        octal.append(str(oct(num))[2:])
        hexadecimal.append(str(hex(num)).upper()[2:])
        binary.append(str(bin(num))[2:])
    return decimal, octal, hexadecimal, binary


def longest_bin_num(n, binary):
    return len(binary[n - 1])


def print_lists(n, decimal, octal, hexadecimal, binary, longest_num):
    for i in range(n):
        print(decimal[i].rjust(longest_num) + octal[i].rjust(longest_num + 1) +
              hexadecimal[i].rjust(longest_num + 1) + binary[i].rjust(longest_num + 1))


def main():
    # variables
    decimal = []
    octal = []
    hexadecimal = []  # capitalized
    binary = []

    n = get_input()
    decimal, octal, hexadecimal, binary = making_lists(n, decimal, octal, hexadecimal, binary)
    longest_num = longest_bin_num(n, binary)
    print_lists(n, decimal, octal, hexadecimal, binary, longest_num)

main()
