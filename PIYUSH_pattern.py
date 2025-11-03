n = 7
for i in range(n):
    # P
    for j in range(n):
        if j == 0 or i == 0 or (j == n - 1 and i <= n // 2) or i == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    # I
    for o in range(n):
        if (o == 3) or i == 0 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end=" ")

    # Y
    for m in range(n):
        if (
            (m == i and m <= n // 2)
            or (m + i == n - 1 and m >= n // 2)
            or (m == 3 and i >= n // 2)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end=" ")

    # U
    for u in range(n):
        if u == 0 or i == n - 1 or u == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end=" ")

    # S
    for s in range(n):
        if (
            (i == 0)
            or (s == 0 and i <= n // 2)
            or i == 3
            or (s == n - 1 and i >= n // 2)
            or i == n - 1
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end=" ")

    # H
    for h in range(n):
        if (h == 0) or h == n - 1 or i == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
