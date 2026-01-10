a = [-19, 20, 21, 22, 23]
b = [-2, 6, 9, 18]
m = len(a)
n = len(b)
i, j = 0, 0
c = []

while i <= m - 1 and j <= n - 1:
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

for k in range(i, m):
    c.append(a[k])

for k in range(j, n):
    c.append(a[k])
print(c)
