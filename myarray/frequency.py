# Count frequency of an element
arr = [1, 2, 2, 3, 2]


def count_frequency(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
    return count


print(count_frequency(arr, 4))
