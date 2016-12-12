import textwrap

print("\n")
string = "This is a very very very very very long string."
print(textwrap.wrap(string, 8))
print("\n")
# output: ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']


st = "This is a very very very very very long string. \n"
print(textwrap.fill(st, 10))
print("\n")
#   'output:'
# This is a
# very very
# very very
# very long
# string.


line = input("Please type the sencence you want to be printed out in columns: ")
number = int(input("Character number of the columns: "))
print(textwrap.fill(line, number))
