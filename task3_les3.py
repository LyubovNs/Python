# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(n1, n2, n3):
    list = [n1, n2, n3]
    list.remove(min(n1, n2, n3))
    return sum(list)

print(my_func(1, 2, 3))