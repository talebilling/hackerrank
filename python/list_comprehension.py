def comprehension_version(a):
    a = [b + 4 if b < 99 else b for b in a]
    print(a)


def add_4_to_list_elements(a):
    for i in range(len(a)):
        if a[i] < 99:
            a[i] += 4
    print(a)


def main(a):
    comprehension_version(a)
    add_4_to_list_elements(a)

a = [1, 2, 3, 4]
main(a)
