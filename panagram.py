# Check if a sentence is a pangram

def is_pangram(sentence):
    sentence = sentence.lower().strip()
    letters = set(sentence)
    print(letters)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in letters:
            return False

    return True

text = "The quick brown foax dog"
if is_pangram(text):
    print("This is a pangram.")
else:
    print("This is not a pangram.")
