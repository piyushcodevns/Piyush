n=7
for i in range(n):
    for j in range(n):
        if i==n//2 or ( i+j==n//2+6 or i-j==n//2-6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )