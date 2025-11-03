arr=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in arr:
    if i %2 ==0:
        even.append(i)
    elif i%2==1:
        odd.append(i)
print("Even array:",even)
print("odd array:",odd)