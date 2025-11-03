row=5
for i in range(5,0,-1):
    for f in range(row-i):
        print(" ",end=" ")
    for h in range(2*i-1):
        print("*",end=" ")
    print()