arr=[1,2,1,0,2,0]
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[j],arr[i]=arr[i],arr[j]
print(arr)