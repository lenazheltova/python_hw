# задание 1 Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = [21, 'may', 19.58, 'homework']
for el in my_list:
    print(f'{el} is {type(el)}')