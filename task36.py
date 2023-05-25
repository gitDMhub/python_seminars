# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
#
def print_operation_table(operation, num_rows=6, num_columns=6):
    print('\nTable 6x6 for the operation:')
    print('{0:1} {1:4d} {2:4d} {3:4d} {4:4d} {5:4d} {6:4d}'.format('', 1, 2, 3, 4, 5, 6), end='')
    for x in range(1, num_rows+1):
#       print('{0:3} {1:4d} {2:4d} {3:4d} {4:4d} {5:4d} {6:4d}'.format(x, operation(x,1), operation(x,2), operation(x,3), operation(x,4), operation(x,5), operation(x,6)))
        print(f'\n{x:2}', end='')
        for y in range(1, num_columns+1):
            print(f'{operation(x,y):5}', end='')

print_operation_table(lambda num_rows, num_columns: round(num_rows/num_columns,2))