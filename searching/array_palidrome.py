arr = [1, 2, 1, 0, 1, 1]
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        sub = arr[i : j + 1]
        if sub == sub[::-1]:
            print(sub)
            break
