class Currency:
    def adjust(self, n):
        if n < 10:
            return "0" + str(n)
        else:
            return str(n)

    def __init__(self, rupees, paisa):
        self.total_paisa = rupees * 100 + paisa

    @property
    def rupees(self):
        return self.total_paisa // 100

    @property
    def paisa(self):
        return self.total_paisa % 100

    def __add__(self, other):
        return Currency(0, self.total_paisa + other.total_paisa)

    def __sub__(self, other):
        if self.total_paisa < other.total_paisa:
            raise ValueError("Insufficient funds!")
        total = self.total_paisa - other.total_paisa
        return Currency(0, total)

    def __ge__(self, other):
        return self.total_paisa >= other.total_paisa

    def __gt__(self, other):
        return self.total_paisa > other.total_paisa

    def __eq__(self, other):
        return self.total_paisa == other.total_paisa

    def __str__(self):
        return f"₹ {self.adjust(self.rupees)}. {self.adjust(self.paisa)}"


if __name__ == "__main__":
    print("Enter first currency:")
    r1 = int(input("Rupees: "))
    p1 = int(input("Paisa: "))
    c1 = Currency(r1, p1)

    print("Enter second currency:")
    r2 = int(input("Rupees: "))
    p2 = int(input("Paisa: "))
    c2 = Currency(r2, p2)

    print("\nFirst Currency:", c1)
    print("Second Currency:", c2)

    c_add = c1 + c2
    print("Addition:", c_add)

    try:
        c_sub = c1 - c2
        print("Subtraction (first - second):", c_sub)
    except ValueError as e:
        print("Subtraction (first - second):", e)

    try:
        c_sub2 = c2 - c1
        print("Subtraction (second - first):", c_sub2)
    except ValueError as e:
        print("Subtraction (second - first):", e)