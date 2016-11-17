def longest(s1, s2):
    s1s2 = s1 + s2
    section = set(s1s2)
    section = ''.join(sorted(section))
    return section

s1 = "aretheyhere"
s2 = "yestheyarehere"
new_str = longest(s1, s2)
print(new_str)
