arr = [4, 0, 4, 9, 0]
search = 4
mode = int(input("Enter the number: "))
found = False
if mode == 1:
    for i in range(len(arr)):
        if arr[i] == search:
            print(f"{search} found on index {i}")
            found = True
            break
    if not found:
        print(f"{search} not found")

elif mode == 2:
    for j in range(len(arr) - 1, -1, -1):
        if arr[j] == search:
            print(f"{search} found on index {j}")
            found = True
            break
    if not found:
        print(f"{search} not found")
elif mode == 3:
    position=[]
    for k in range(len(arr)):
        if arr[k]==search:
            position.append(k)
            found=True
    if found:
        print(f"{search} found on index {position}")
    if not found:
        print(f"{search} not found")
        
else:
    print("Invalid mode")