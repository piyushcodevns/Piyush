#Reverse an array.
numbers = [2, 9, 0, 7, 6, 5, 1, 2]
reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print("Reversed array is:", reversed_numbers)