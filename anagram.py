# Check if two strings are anagrams.
def are_anagrams(str1, str2):
    str1 = str1.lower().strip()
    str2 = str2.lower().strip()
    print(f"Comparing {str1} and {str2}")
    m = len(str1)
    n = len(str2)
    if m != n:
        return False
    for i in range(m):
        ch1 = str1[i]
        ch2 = str2[i]
        if ch1 not in str2:
            return False
        if ch2 not in str1:
            return False

    return True


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
if not are_anagrams(word1, word2):
    print("This is not Anagram.")
else:
    print("This is Anagram.")
