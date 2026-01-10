units =["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten=["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty"]

def number_to_word(number):
    if number<10:
        return units[number]
    elif number<20:
        teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
        return teens[number-10]
    elif number <100 :
        return ten[number//10] + (" " + units[number%10] if number %10!=0 else "")        
    
    
for i in range(0,100):
    print(number_to_word(i))
        