arr = [10, 5, 20, 8, 15]

max1 = max(arr)
max2 = -1
# print(max2)
for x in arr:
    # print(x)
    if x != max1 and x > max2:
        max2 = x

print("2nd max =", max2)
