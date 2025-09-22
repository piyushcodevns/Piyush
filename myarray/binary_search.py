arr=[1,2,3,4,5,6]
def binary_search_iterative(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(binary_search_iterative(arr, 2))