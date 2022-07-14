# Реализуйте алгоритм перемешивания списка.

from random import choice


def peremeshat(a = []):
    b = []
    for i in range(len(a)):
        vrem = choice(a)
        b.append(vrem)
        a.remove(vrem)
    print(b)


spisok = list(range(10))
print(spisok)
peremeshat(spisok)
