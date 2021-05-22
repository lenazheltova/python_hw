#задание 5. Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.


my_list = [7, 5, 3, 3, 2]
print(my_list)
new_number = int(input('Enter new number:')) #здесь он вводит новое число
count = my_list.count(new_number) #здесь я узнаю кол-во элментов со значением нового числа
for element in my_list: #для элемента в моем списке выполнить что ниже
    if count > 0: #если новое число уже есть в списке, то
        i = my_list.index(new_number) #получить i - позицию первого элемента со значением нового числа
        my_list.insert(i+count, new_number) #я вставляю новое число на позицию + количество имеющихся)
        break
    else:
        if new_number > element:
            j = my_list.index(element) #получаю y - позицию элемента меньше нового
            my_list.insert(j, new_number)
            break
        if new_number < element:
            my_list.append(new_number)
            break
print(my_list)