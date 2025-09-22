def unique_char(s):
    for char in reversed(s):
        if s.count(char) == 1:
            return char
    return None
print(unique_char("swiss"))  # Output: "w"
print(unique_char("repeater"))  # Output: "r"
print(unique_char("aabbcc"))  # Output: None