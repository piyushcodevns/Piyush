row = 5
for i in range(1, row + 1):
    for j in range(row - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()



for l in range(4,0,-1):
    for h in range(row-l):
        print(" ",end=" ")
    for n in range(2*l-1):
        print("*",end=" ")
    print()