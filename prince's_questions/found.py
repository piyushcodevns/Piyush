arr=[10,20,30,40,50,60]
search=50
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print(f"{search} found on index {i}")
        found=True
        break
if not found:
    print(f"{search} not found")