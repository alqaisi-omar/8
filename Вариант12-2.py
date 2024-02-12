def subtract_last_row(matrix):
    last_row = matrix[-1]
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i])):
            matrix[i][j] -= last_row[j]

# Пример матрицы
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

subtract_last_row(matrix)

print("Матрица после преобразования:")
for row in matrix:
    print(row)
