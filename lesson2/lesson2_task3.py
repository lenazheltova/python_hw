# задание 3 Пользователь вводит месяц в виде целого числа от 1 до 12
# Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

seasons_list = ['winter', 'spring', 'summer', 'fall']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'fall'}
month = int(input('Input number of the month'))
if month == 1 or month == 2 or month == 12:
    print(seasons_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
else:
    print(seasons_dict.get(4))