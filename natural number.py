a = 1234
reverse = 0
while True:
    if a == 0:
        break
    else:
        digit = a % 10
        reverse = reverse * 10 + digit
        a = a // 10
print(reverse)
