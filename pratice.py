units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

tens = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

teens = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]


def number_to_word(number):
    if number < 10:
        return units[number]
    elif number < 20:
        return teens[number - 10]
    elif number < 100:
        return tens[number // 10] + (
            "" if number % 10 == 0 else " " + units[number % 10]
        )

    elif number < 1000:
        return (
            units[number // 100]
            + " hundred"
            + ("" if number % 100 == 0 else " " + number_to_word(number % 100))
        )
    elif number < 10000:
        return (
            units[number // 1000]
            + " thousand"
            + ("" if number % 1000 == 0 else " " + number_to_word(number % 1000))
        )
    else:
        return "wrong"


number = int(input("Enter the number (0-999): "))
print(number_to_word(number))
