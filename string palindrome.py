text = "madaml"
palindrome=""
for i in range(len(text) - 1, -1, -1):
    palindrome+=text[i]
if text==palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
        