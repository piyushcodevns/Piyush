n = 7  # total rows
for i in range(n):
    for j in range(n):
        if j==0 or i + j == n//2+1 or i - j == n//2-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
