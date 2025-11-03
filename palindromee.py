def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

x=int(input('Enter the integer: '))
if isPalindrome(x):
   print('+vr : ',x,'-ve :',x)
else:
    up=x+1
    while not isPalindrome(up):
        up+=1
    down=x-1
    while down<=0 and not isPalindrome(down):
        down-=1

    print('+ve :',up, '-ve :',down)