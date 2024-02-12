def max_abs_value(matrix):
    max_val = None
    max_index = None
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if max_val is None or abs(matrix[i][j]) > abs(max_val):
                max_val = matrix[i][j]
                max_index = (i, j)
    return max_val, max_index

def remove_row_and_column(matrix, index):
    i, j = index
    n = len(matrix)
    new_matrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
    return new_matrix

# Пример квадратной матрицы
matrix = [[1, 2, 3],
          [4, -5, 6],
          [7, 8, 9]]

max_val, max_index = max_abs_value(matrix)
print("Наибольший по модулю элемент:", max_val)

new_matrix = remove_row_and_column(matrix, max_index)
print("Квадратная матрица порядка n - 1:")
for row in new_matrix:
    print(row)
