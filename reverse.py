n = 1234
rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
print("reverse =", rev)

text = "hello"
rev = text[::-1]
print("Reverse=", rev)

num = [10, 20, 30, 40, 50]
num.reverse()
print("reverse: ", num)

arr = [1, 2, 3, 4, 5, 6]
rev = []
for i in range(len(arr) - 1, -1, -1):
    rev.append(arr[i])
print("reverse: ", rev)
