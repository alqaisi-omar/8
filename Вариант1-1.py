N = 4
A = [[2, -3, 4, 5],
     [1, 6, -2, 8],
     [3, 7, 2, 9],
     [4, 1, 3, -5]]

sum_positive = 0
count_positive = 0

for i in range(N):
    for j in range(i + 1, N):  # только элементы над главной диагональю
        if A[i][j] > 0:
            sum_positive += A[i][j]
            count_positive += 1

print("Сумма положительных элементов над главной диагональю:", sum_positive)
print("Число положительных элементов над главной диагональю:", count_positive)
