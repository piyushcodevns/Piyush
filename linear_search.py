arr = [10, 20, 30, 10, 20, 10]
mode = int(input("Enter the mode(1/2/3): "))
search = int(input("Enter element to search: "))

found = False

if mode == 1:
    for i in range(len(arr)):
        if arr[i] == search:
            print(f"{search} found at index {i}")
            found = True
            break
    if not found:
        print(f"{search} not found")

elif mode == 2:
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == search:
            print(f"{search} found at index {i}")
            found = True
            break
    if not found:
        print(f"{search} not found")

elif mode == 3:
    positions = []
    for i in range(len(arr)):
        if arr[i] == search:
            positions.append(i)
            found = True
    if found:
        print(f"{search} found at indices {positions}")
    else:
        print(f"{search} not found")

else:
    print("Invalid mode")