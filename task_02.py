# Задача 2: Найдите сумму цифр трехзначного числа.
#
n = int(input('Введите трехзначное число: '))
sum = n//100 + n//10%10 + n%10
print("Cумма цифр трехзначного числа = ", sum)