# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def numbers(*args):
    return max(args)

print(numbers(1, 2, 5, 78))


def numeric(one, two, tree):
    return max(one, two, tree)

print(numeric(2, 600, 5))