vowel=("a","e","i","o","u")
consonent=("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
def read_vowels_and_consonenta_in_paragraph():
    paragraph = input("Enter a paragraph: ")
    paragraph = paragraph.lower()
    vowels_count = 0
    consonents_count = 0
    for char in paragraph:
        if char in vowel:
            vowels_count += 1
        elif char in consonent:
            consonents_count += 1
    print("Number of vowels:", vowels_count)
    print("Number of consonents:", consonents_count)
read_vowels_and_consonenta_in_paragraph()