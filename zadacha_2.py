# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 
# Пример:
# 
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def nabor_proizved(n = []):
    nabor = []
    proizved = 1
    for i in range(1, n+1):
        proizved = proizved * i
        nabor.append(proizved)
    print(nabor)

n = int(input('Введите число n ->'))
nabor_proizved(n)


