n = 3
m = 4
matrix = [[3, 7, 2, 8],
          [5, 1, 9, 4],
          [6, 2, 4, 7]]

new_matrix = []

for row in matrix:
    min_val = min(row)
    new_row = []
    for num in row:
        if num == min_val:
            new_row.append(0 if num % 2 == 0 else 1)
        else:
            new_row.append(num)
    new_matrix.append(new_row)

print("Новая матрица:")
for row in new_matrix:
    print(row)

