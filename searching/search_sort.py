arr = [4, 0, 4, 0, 9]
n = len(arr)
small = arr[0]
for i in range(1, n):
    if arr[i] < small:
        small = arr[i]

second = arr[0]
for i in range(n):
    if arr[i] > small:
        second = arr[i]
        break

for i in range(n):
    if arr[i] > small and arr[i] < second:
        second = arr[i]

result = [small, second]
print(result)

