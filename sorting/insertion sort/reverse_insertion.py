arr=[4,6,5,3,7,6,8,9]
n = len(arr)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(arr)
