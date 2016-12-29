'''
Sample Input:
3
1 0
2 $
3 1

Sample Output:
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''


def main():
    for i in range(int(input())):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except Exception as e:
            print("Error Code:", e)

main()
