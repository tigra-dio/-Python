"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

ls = ['Имя', 123, 'Фамилия', 10.23, True]
l0 = (ls[0])

print(type(ls))
print(type(l0)) or print(type(ls[0]))
print(type(ls[1]))
print(type(ls[2]))
print(type(ls[3]))
print(type(ls[4]))

'''
'''

my_list = [12, None, -77, 'True', True, 9.5]
for el in range(len(my_list)):
    print(type(my_list[el]))

