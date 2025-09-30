num=int(input("Enter the integer: "))
cleaned_text=str(num)
if cleaned_text == cleaned_text[::-1]:
 print("Palindrome Number")
else: 
 print("Not palindrome number")