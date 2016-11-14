# input:
# 5
# 2 3 6 6 5

n = int(input())
my_list = input().split()
my_list = [int(item) for item in my_list]
larger = max(my_list)
second_larger = min(my_list)

for i, item in enumerate(my_list):
    if second_larger < item < larger:
        second_larger = my_list[i]
print(second_larger)
