# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
a = int(input('Enter a: '))
b = int(input('Enter b: '))

def sumAB(a, b):
    a += 1
    b -= 1
    if b == 0:
        return a
    else:
        return sumAB(a, b)

print(f'{a} + {b} =', sumAB(a, b))