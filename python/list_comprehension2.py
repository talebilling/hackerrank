'''
Let's learn about list comprehensions! You are given three integers  and  representing the
dimensions of a cuboid along with an integer . You have to print a list of all possible
coordinates given by  on a 3D grid where the sum of  is not equal to .

Input Format
Four integers  and  each on four separate lines, respectively.
'''

x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n
