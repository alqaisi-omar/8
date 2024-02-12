n = 3
m = 4
matrix = [[5, 2, 7, 1],
          [8, 4, 3, 6],
          [9, 2, 1, 5]]

for row in matrix:
    row.sort()

print("Матрица после упорядочивания по возрастанию:")
for row in matrix:
    print(row)
