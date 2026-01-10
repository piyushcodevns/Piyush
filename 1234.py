def number_to_words(num):
    ones = ["","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
             "seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    if num == 0:
        return "zero" 
    words = ""
    if num // 1000 > 0:
        words += ones[num // 1000] + " thousand "
        num %= 1000

    if num // 100 > 0:
        words += ones[num // 100] + " hundred "
        num %= 100

    if num > 0:
        if num < 10:
            words += ones[num]
        elif num < 20:
            words += teens[num - 10]
        else:
            words += tens[num // 10] + " "
            if num % 10 > 0:
                words += ones[num % 10]

    return words.strip()

print(number_to_words(1234))