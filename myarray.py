#Find the largest/smallest element in an array.
numbers=[-7,-6,-5,-4,-3,-2,-9]
largest=numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest number is:", largest)
smallest=numbers[0]
for j in numbers:
    if j < smallest:
        smallest = j
print("Smallest number is:", smallest)