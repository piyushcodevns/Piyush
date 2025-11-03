arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 20
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == target:
                print("pairs:", arr[i], arr[j], arr[k])
    break
