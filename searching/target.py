arr = [4, 0, 4, 9, 0]
target = 8
found=False
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])
            found=True
if not found:
    print("Not found")
