# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 
# Пример:
# 
# - 6782 -> 23
# - 0,56 -> 11

from turtle import st


a = float(input('Введите вещественное число -> ')) # условие должно быть соблюдено
b = str(a)
b = b.replace('.','')
sum = 0
for i in b:
    sum = sum + int(i)
print(sum)

# Это самое тупое решение но другого я не придумал