arr = [10,20,30,40,50]
x = 30
low = 0
high = len(arr)-1
found = False
while low <= high:
    mid = (low + high)//2
    if arr[mid] == x:
        found = True
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
print(found)  # True
