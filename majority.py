arr=[1,1,2,1,3,5,1]
n=len(arr)
count=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            count+=1
            print(i,count)