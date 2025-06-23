# Implement left/right rotation of an array.
numbers = [1, 2, 3, 4, 5, 6, 7]
k=6
left_rotated = numbers[k:] + numbers[:k]
right_rotated = numbers[-k:] + numbers[:-k]
print("Left rotated array:", left_rotated)
print("Right rotated array:", right_rotated)
