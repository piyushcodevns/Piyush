row=5
for i in range(1,row+1):
    for s in range(i):
        print("*",end="")
    print()
    


row=5
for i in range(1,row+1):
    for s in range(row-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
    


row=5
for i in range(1,row+1):
    for s in range(row-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
    
    

row=5
for i in range(1,row):
    for s in range(row-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
    
for l in range(5,0,-1):
    for k in range(row-l):
        print(" ",end="")
    for g in range(2*l-1):
        print("*",end="")
    print()