arr=[1,2,3,4,5,6,8,9,10]
n=len(arr)
position=0
for i in range(1,n+1):
    position+=1
    if i not in arr:
        print(f"{i} found at position {position}")
        break
else:
    print("Invalid number")