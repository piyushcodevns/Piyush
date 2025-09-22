# Find index of first occurrence
arr=[4,4,4]
def first_occurrence(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
print(first_occurrence(arr,4))