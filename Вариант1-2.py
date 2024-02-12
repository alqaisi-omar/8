N = 3
M = 4
B = [[2, 5, 7, 3],
     [1, 9, 4, 6],
     [8, 2, 3, 5]]

for i in range(N):
    min_val = min(B[i])
    max_val = max(B[i])
    min_index = B[i].index(min_val)
    max_index = B[i].index(max_val)
    B[i][0], B[i][min_index] = B[i][min_index], B[i][0]  # поменять минимальный элемент с первым
    B[i][-1], B[i][max_index] = B[i][max_index], B[i][-1]  # поменять максимальный элемент с последним

print("Матрица B после обработки:")
for row in B:
    print(row)
