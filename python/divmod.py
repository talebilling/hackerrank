'''
Built-in func, which takes 2 arguments and and returns a tuple containing the quotient of first and then the remainder 
Sample Input:
177
10

Sample Output:
17
7
(17, 7)
'''

a = int(input())
b = int(input())
print("{0}\n{1}\n({0}, {1})".format(*divmod(a, b)))
