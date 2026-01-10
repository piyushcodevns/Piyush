arr = [1, 2, 2, 3, 3, 3, 4]
duplicate = []

for i in arr:
    if arr.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print(duplicate)
