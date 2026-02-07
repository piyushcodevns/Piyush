arr=[5,8,9,10,-1,6,13]
target=19
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
            print(i,j)
            break