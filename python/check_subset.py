'''
input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

output:
True
False
False
'''


def main():
    result = []
    for i in range(int(input())):
        a = int(input())
        A = set(input().split())
        b = int(input())
        B = set(input().split())
        if B.intersection(A) == A:
            result.append("True")
        else:
            result.append("False")
    print("\n".join(result))

main()
