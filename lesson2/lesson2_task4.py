# задание 4 Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.


user_string = input('Please make a list of some words, use spaces, not commas: ')
user_list = user_string.split()
for i, el in enumerate(user_list, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i} - {el}")
