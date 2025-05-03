# a, b = 2, 3

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Modulus:", a % b)
# print("Multiplication:", a * b)
# print("x to the power y:", a**b)


# a = float(input("\nEnter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))
    
# s = (a + b + c) / 2
# area = s * (s - a) * (s - b) * (s - c)
# area = area**0.5
# print("Area of triangle is:", area)


p = float(input("\nEnter principal amount (P): "))
r = float(input("Enter rate of interest (R) : "))
t = float(input("Enter time (T) in years: "))

si = (p * r * t) / 100
print("Simple Interest is:", si)

ci = p * (1 + r/100)**t - p
print("Compound Interest is:", ci)