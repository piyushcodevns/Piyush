# Find first occurrence using Binary Search

arr = [1, 2, 2, 2, 3, 4, 5]
def binary_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
print(binary_first_occurrence(arr, 2))