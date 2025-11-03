arr=[1,1,2,2,2,3,4,5,5]
dublicate=[]
for i in arr:
    if i not in dublicate:
        dublicate.append(i)
print(dublicate)