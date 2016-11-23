'''
input
4
2 4 5 9
4
2 4 11 12
Output the symmetric difference integers in ascending order, one per line:
5
9
11
12
'''


def main():
    m, n = get_inputs()
    m, n = make_sets(m, n)
    united_set = make_difference_and_union(m, n)
    print_united_set(united_set)


def get_inputs():
    m_len = int(input())
    m = input().split()
    n_len = int(input())
    n = input().split()
    return m, n


def make_sets(m, n):
    m = set(map(int, m))
    n = set(map(int, n))
    return m, n


def make_difference_and_union(m, n):
    diff_m_n = m.difference(n)
    diff_n_m = n.difference(m)
    united_set = sorted(diff_m_n.union(diff_n_m))
    return united_set


def print_united_set(united_set):
    for i in united_set:
        print(i)

main()
