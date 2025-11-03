arr = [4, 3, 2, 5, 6]
n = int(input("Enter which smallest number you want: "))
for i in range(n):
    small = 9
    for j in arr:
        if j < small:
            small = j
    arr.remove(small)
print("The", n, "smallest number is:", small)