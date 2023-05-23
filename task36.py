# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
#
def print_operation_table(operation, num_rows=6, num_columns=6):
    print('\nTable 6x6 for the operation:')
    print('{0:3} {1:4d} {2:4d} {3:4d} {4:4d} {5:4d} {6:4d}'.format('', 1, 2, 3, 4, 5, 6))
    for x in range(1, 7):
        print(f'{x:3} {operation(x,1):4} {operation(x,2):4} {operation(x,3):4} {operation(x,4):4} {operation(x,5):4} {operation(x,6):4}')
#        print('{0:3} {1:4d} {2:4d} {3:4d} {4:4d} {5:4d} {6:4d}'.format(x, operation(x,1), operation(x,2), operation(x,3), operation(x,4), operation(x,5), operation(x,6)))

print_operation_table(lambda r, c: round(r/c,1))