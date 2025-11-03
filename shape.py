# n = 3
# for row in range(1, n):
#     for space in range(1, n - row + 1):
#         print(" ", end=" ")
#     for star in range(1, row + 1):
#         print(star, end=" ")
#     for star in range(1, row):
#         print(row - star, end=" ")
#     print()

# for row in reversed(range(1, n + 1)):
#     for space in range(1, n - row + 1):
#         print(" ", end=" ")
#     for star in range(1, row + 1):
#         print(star, end=" ")
#     for star in range(1, row):
#         print(row - star, end=" ")
#     print()

# hollow square pattern
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()