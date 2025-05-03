class Currency:
    def __init__(self, rupees, paisa):
        self.rupees = rupees
        self.paisa = paisa

    def __str__(self):
        return f"{self.rupees} rupees and {self.paisa} paisa"

    def add(self, other):
        paisa = self.paisa + other.paisa
        rupees = self.rupees + other.rupees + (paisa // 100)
        return Currency(rupees, paisa % 100)

    def subtract(self, other):
        total_self = self.rupees * 100 + self.paisa
        total_other = other.rupees * 100 + other.paisa
        if total_self < total_other:
            raise ValueError("Insufficient balance")
        remaining = total_self - total_other
        return Currency(remaining // 100, remaining % 100)