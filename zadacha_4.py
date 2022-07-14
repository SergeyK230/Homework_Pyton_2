# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 


def proizvedenie(spisok = [], poz = str):
    spisok_list = poz.split(' ')
    answer = 1
    for i in spisok_list:
        print(f'{spisok[int(i)]} ', end = '')
        answer = answer * spisok[int(i)]
    return answer


n = int(input('Введите число n -> '))
if n < 0:
    n = -n

spisok = list(range(-n,n+1))

pozitcii = input('Введите индексы элементов через пробел -> ')

print(f'-> {proizvedenie(spisok, pozitcii)}')



