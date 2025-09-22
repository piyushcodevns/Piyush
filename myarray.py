#Find the largest/smallest element in an array.
numbers=[1,2,3,4,5,6,7]
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