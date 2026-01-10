a = [-19, 20, 21, 22, 23]
b = [-2, 6, 9, 18]
m = len(a)
n = len(b)
i, j = m - 1, n - 1
c = []

while i >= 0 and j >= 0:
    if a[i] > b[j]:
        c.append(a[i])
        i -= 1
    else:
        c.append(b[j])
        j -= 1

for k in range(i, -1, -1):
    c.append(a[k])

for k in range(j, -1, -1):
    c.append(b[k])

print(c)
