n=7
for i in range(n):
    for j in range(n):
        if(i==j and j<=n//2) or (i+j==n-1 and i<=n//2)or(j==3 and i>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()