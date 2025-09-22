# Find index of last occurrence

arr=[4,4,4]
def last_occurrence(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1
print(last_occurrence(arr, 4))