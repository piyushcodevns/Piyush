arr=[11,2,4,3,12]
print("Array element is:")
for i in range(len(arr)):
    print(arr[i])
    
# Find the smallest element and print it.  2
# Find the position of the smallest number and print it. 1

smallest=arr[0]
pos=0
for i in range(len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]
        pos=i
print("Smallest element in array is:",smallest)
print("Position of smallest element in array is:",pos)

# Swap the smallest number with the 0th element. [11,2,4,3,12]=[2,11,4,3,12]
arr[0],arr[pos]=arr[pos],arr[0]
print("Swapped Array:")
for i in range(len(arr)):
    print(arr[i])
    
    
# Repeat for all numbers in the array. 
a = [11, 2, 4, 3, -2]
n = len(a)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]
    print(a)