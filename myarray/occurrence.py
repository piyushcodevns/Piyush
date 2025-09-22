# Search all occurrences of an element
arr = [1, 2, 3]
def find_all_occurrences(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices
print(find_all_occurrences(arr, 7))