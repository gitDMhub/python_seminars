# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#
import random
n = int(input('Enter the 1st list size: '))
m = int(input('Enter the 2nd list size: '))
list_n = [random.randint(1,11) for _ in range(n)]
list_m = [random.randint(1,11) for _ in range(m)]
list_d = set()
print(list_n)
print(list_m)
for num in list_n:
    if num in list_m:
        list_d.add(num)
print(list_d)
