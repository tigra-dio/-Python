"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

user = (input('Введите несколько элементов через пробел: ')).split()
# Нумерованные списки
for ind, el in enumerate(user, 1):
    if int(len(el)) > 10:
        print(ind, el[0:10])
    else:
        print(ind, el)
