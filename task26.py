# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
a = int(input('Enter A: '))
b = int(input('Enter B: '))

def powerA2B(a, b):
    if b == 0:
        return 1
    else:
        return a * powerA2B(a, b-1)

print(f'Number {a} raised to the power of {b}: ', powerA2B(a, b))