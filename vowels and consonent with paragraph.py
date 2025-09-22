vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
consonent = (
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
    "B",
    "C",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "X",
    "Y",
    "Z",
)


def count_vowel_consonent():
    paragraph = input("Enter the paragraph:")
    count_vowel = 0
    count_consonant = 0
    for char in paragraph:
        if char in vowel:
            count_vowel += 1
        elif char in consonent:
            count_consonant += 1
        print("Number of vowels: ", count_vowel)
        print("Number of consonants: ", count_consonant)


count_vowel_consonent()
