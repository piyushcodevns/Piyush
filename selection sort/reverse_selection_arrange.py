arr = [4, 5, 7, 2, 4, 9, 10, -2]
n = len(arr)

for i in range(0, n-1):
    min = arr[i]
    minpos = i
    for j in range(i+1, n):
        if arr[j] < min:
            min = arr[j]
            minpos = j
    arr[i], arr[minpos] = arr[minpos], arr[i]
    print(arr)
