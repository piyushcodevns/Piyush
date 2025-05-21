class Algebra():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y

    def modulus(self):
        return self.x // self.y

    def power(self):
        return self.x ** self.y
    
    def il(self):
        return self.x < self.y
    
    def gt(self):
        return self.x > self.y
    
    def eq(self):
        return self.x == self.y
    
    def le(self):
        return self.x <= self.y
    
    def ge(self):
        return self.x >= self.y
    
    def ne(self):
        return self.x != self.y
    
    def __isub__(self):
        return self.x - self.y
    
    def __iadd__(self):
        return self.x + self.y
    
    def __imul__(self):
        return self.x * self.y
    
    def __itruediv__(self):
        return self.x / self.y
    
    def __imod__(self):
        return self.x % self.y
    
    def __ipow__(self):
        return self.x ** self.y
    
    def __ifloordiv__(self):
        return self.x // self.y
    

x = 56
y = 78
alg = Algebra(x, y)

print("Value of X:", alg.x)
print("Value of Y:", alg.y)
print("Addition:", alg.addition())
print("Subtraction:", alg.subtraction())
print("Multiplication:", alg.multiplication())
print("Division:", alg.division())
print("Modulus:", alg.modulus())
print("Power:", alg.power())
print("IL (x < y):", alg.il())
print("GT (x > y):", alg.gt())
print("EQ (x == y):", alg.eq())
print("LE (x <= y):", alg.le())
print("GE (x >= y):", alg.ge())
print("NE (x != y):", alg.ne())
print("In-place Subtraction (x -= y):", alg.__isub__())
print("In-place Addition (x += y):", alg.__iadd__())
print("In-place Multiplication (x *= y):", alg.__imul__())
print("In-place Division (x /= y):", alg.__itruediv__())
print("In-place Modulus (x %= y):", alg.__imod__())
print("In-place Power (x **= y):", alg.__ipow__())
print("In-place Floor Division (x //= y):", alg.__ifloordiv__())