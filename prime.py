x=2
for i in range(2,17):
    print(x,end=", ")
    x=x+1
    while True:
        for j in range(2,int(x**0.5)+1):
            if x%j==0:
                x=x+1
                break
        else:
            break