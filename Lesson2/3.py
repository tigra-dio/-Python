"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

months = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
# get
user = int(input('Введите число месяца от 1 до 12: '))
if user > 12 or user < 1:
    print("Такого месяца не существует")
elif user == 12 or user == 1 or user == 2:
    print(months.get(1))
elif user == 3 or user <= 5:
    print(months.get(2))
elif user == 6 or user <= 8:
    print(months.get(3))
elif user == 9 or user <= 11:
    print(months.get(4))

