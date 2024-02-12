def find_matching_rows_and_columns(matrix):
    matching_indices = []
    n = len(matrix)
    for k in range(n):
        if matrix[k] == [matrix[i][k] for i in range(n)]:
            matching_indices.append(k)
    return matching_indices

# Пример квадратной матрицы
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matching_indices = find_matching_rows_and_columns(matrix)
print("Индексы строк и столбцов, которые совпадают:", matching_indices)
