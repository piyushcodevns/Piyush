arr = [38, 26, 22, 1, 9, 14, 33]

longest = []
current = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] >= arr[i-1]: 
        current.append(arr[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [arr[i]]

if len(current) > len(longest):
    longest = current

print("Longest non-decreasing sequence:", longest)
print("Length:", len(longest))
