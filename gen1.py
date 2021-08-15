# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

fruits = ['apple', 'banana', 'melon', 'lemon', 'orange']
fruits_new = ['apple', 'pear', 'orange']

all = [fruit for fruit in fruits if fruit in fruits_new]

print(all)