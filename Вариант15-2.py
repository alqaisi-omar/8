def find_max_sum_row(matrix):
    max_sum = None
    max_sum_row = None
    for row in matrix:
        if all(element % 2 != 0 for element in row):  # проверяем, что все элементы строки нечетные
            row_sum = sum(abs(element) for element in row)  # считаем сумму модулей элементов строки
            if max_sum is None or row_sum > max_sum:
                max_sum = row_sum
                max_sum_row = row
    return max_sum_row

# Пример матрицы
matrix = [[1, 3, 5],
          [7, 9, 11],
          [2, 4, 6],
          [8, 10, 12]]

max_sum_row = find_max_sum_row(matrix)
print("Строка с максимальной суммой модулей элементов среди строк с нечетными элементами:")
print(max_sum_row)
