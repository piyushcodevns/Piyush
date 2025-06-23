# Remove duplicates from a sorted array.
numbers = [1, 1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)
print("Array after removing duplicates:", unique_numbers)