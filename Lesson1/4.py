# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

# Первый вариант с помощью интернета (с арифметикой беда)
num = int(input('Введите целое положительное число: '))
ls = []
while num > 10:
    ls.append(num % 10)
    num //= 10
max_num = max(ls)

print(max_num)


# Второй вариант с помощью интернета
num = int(input('Введите целое положительное число: '))
string = str(num)
ls = list(map(int, string))
max_num = max(ls)

print(max_num)