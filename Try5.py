# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = ['yes', True, 5.6, 87, [4, 4, 5], {'hi', 5}, (True, 3.33)]
print(list)

for item in list:
    print(type(item))