# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# 
# Пример:
# 
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def zapolnenie(n = int):
    spisok = []
    for i in range(1, n+1):
        a = round((1+1/i)**i, 2)
        spisok.append(a)
    return spisok

def summa(n = []):
    sum = 0
    for i in range(len(n)):
        sum = sum + n[i]
        print(f'{i+1} : {sum}')


n = int(input('Введите число n -> '))
spisok = zapolnenie(n)
summa(spisok)
