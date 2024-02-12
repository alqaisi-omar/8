def count_and_max_divisible(matrix, k):
    count = 0
    max_divisible = None
    for row in matrix:
        for num in row:
            if num % k == 0:
                count += 1
                if max_divisible is None or num > max_divisible:
                    max_divisible = num
    return count, max_divisible

# Пример квадратной матрицы
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
k = 3

count, max_divisible = count_and_max_divisible(matrix, k)
print("Число элементов, кратных", k, ":", count)
print("Наибольший элемент, кратный", k, ":", max_divisible)
