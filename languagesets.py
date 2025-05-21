hindi = {"Dhoni", "Virat", "Rohit"}
english = {"Virat", "Rohit"}
french = {"Dhoni", "Virat", "Sachin"}
#  Find people knowing 3 languages, 2 languages, 1 language, and 0 languages

# 3 languages
three = hindi & english & french

# 2 languages (in any two, but not all three)
two = ((hindi & english) | (english & french) | (hindi & french)) - three

# 1 language (only in one)
one = (hindi ^ english ^ french) - two - three

# 0 languages (if you have a master list, otherwise empty)
master = hindi | english | french 
zero = set()

print("3 languages:", three)
print("2 languages:", two)
print("1 language:", one)
print("0 languages:", zero)