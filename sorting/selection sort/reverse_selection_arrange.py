arr = [4, 5, 7, 2, 4, 9, 10, -2]
n = len(arr)

for i in range(n):
    maxpos = i
    for j in range(i + 1, n):
        if arr[j] > arr[maxpos]:
            maxpos = j
    arr[i], arr[maxpos] = arr[maxpos], arr[i]
    print(arr)
