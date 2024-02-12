def find_rows_and_multiply(matrix, c, d):
    matching_rows = []
    for i, row in enumerate(matrix):
        if c in row:
            matching_rows.append(i)
            matrix[i] = [element * d for element in row]
    return matching_rows

# Пример матрицы
R = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

c = 5
d = 2

matching_rows = find_rows_and_multiply(R, c, d)
print("Номера строк с элементом", c, "и их умножение на", d, ":", matching_rows)
print("Матрица после преобразования:")
for row in R:
    print(row)
