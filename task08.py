# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
n = int(input('Введите ширину шоколадки в дольках:'))
m = int(input('Введите длину шоколадки в дольках:'))
k = int(input('Сколько долек нужно отломить за 1 раз:'))
if (k < m*n and (k%m == 0 or k%n == 0)):
    print("Можно!")
else:
    print("Нельзя!")