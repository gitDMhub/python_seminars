# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#
import random
listt = [random.randint(1,11) for i in range(11)]
print(listt)
minn = int(input('Enter the minimum: '))
maxx = int(input('Enter the maximum: '))
for i in range(10):
    val = listt[i]
    if val>=minn and val<=maxx:
        print(i, end=' ')
