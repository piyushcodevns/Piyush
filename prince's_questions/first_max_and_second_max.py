arr=[0,-90,15,17,20,9]
first_min=arr[0]
second_min=arr[0]
for i in arr:
    if i<first_min:
        second_min=first_min
        first_min=i
    elif i<second_min and i!=first_min:
        second_min=i
print("First minimum element is:",first_min)
print("Second minimum element is:",second_min)