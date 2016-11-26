'''
Input:
5
12 9 61 5 14
Output: True
help: 
In [1]: lst = range(10)
In [2]: all( type(i) is int for i in lst )
Out[2]: True
'''

n_len, n = int(input()), input().split()
print(all(int(i) > 0 for i in n) and any(n[index] == (n[index][::-1]) for index in range(len(n))))


'''
first solution:
def main():
    n_len, n = int(input()), list(map(int, input().split()))
    string_list = list(map(str, n))
    boolean = all(i > 0 for i in n)
    result = False
    if boolean is True:
        for index in range(len(string_list)):
            string = string_list[index]
            reserved_string = string[::-1]
            if string == reserved_string:
                result = True
    print(result)
main()
'''
