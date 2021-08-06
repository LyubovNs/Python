#  Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
i = 0
while i <= len(my_list_1):
    for item in my_list_2:
        if item in my_list_1:
            my_list_1.remove(item)
    i += 1
print(my_list_1)
