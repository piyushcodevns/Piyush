a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)  
print("Intersection:", a & b)
print("Difference (a - b):", a - b) 
print("Symmetric Difference:", a ^ b)
a.add(10)
print("After adding 10 to a:", a)
a.remove(2)
print("After removing 2 from a:", a)
b.discard(5)
print("After discarding 5 from b:", b)
b.discard(7)  # No error if 7 is not present
print("After discarding 7 from b (no error):", b)