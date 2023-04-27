# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#
a1 = int(input('Enter the 1st number: '))
n = int(input('Enter the quantity: '))
d = int(input('Enter the step: '))

print(ap := [a1 + i*d for i in range(0,n)])