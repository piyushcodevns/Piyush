matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

n = len(matrix)

right_sum = 0
left_sum = 0

for i in range(n):
    right_sum += matrix[i][i]
    left_sum += matrix[i][n - i - 1]

print("Right Diagonal Sum:", right_sum)
print("Left Diagonal Sum:", left_sum)
 