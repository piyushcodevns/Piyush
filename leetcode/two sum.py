arr=[3,2,4]
n=len(arr)
target=6
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
            print([i,j])