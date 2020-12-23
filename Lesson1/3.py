# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num1 = int(input('Введите число "n": '))
string = str(num1)
num2 = string + string
num3 = num2 + string
summ = num1 + int(num2) + int(num3)

print(summ)
