# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Первый вариант

seconds = int(input('Введите время в секундах: '))
hour = seconds // 3600
minute = (seconds // 60) % 60
second = seconds % 60

print('Ваше время -', f'{hour:02d}:{minute:02d}:{second:02d}')

# Второй вариант не понял как

# seconds = int(input('Введите время в секундах: '))
# import datetime
# str(datetime.timedelta(seconds))
#
# print()
