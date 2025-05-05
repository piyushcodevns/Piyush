class Currency:
    def __init__(self, rupees, paisa):
        self.paisa = rupees*100 + paisa
        

    def __str__(self):
        rs=self.paisa//100 
        ps=self.paisa % 100
        return f"₹ {rs}.{ps}"

    def __add__(self, other):
        paisa = self.paisa + other.paisa
        # rupees = self.rupees + other.rupees + (paisa // 100)
        return Currency(0, paisa)

    def subtract(self, other):
        if self.paisa < other.paisa:
            raise ValueError("Insufficient balance")
        remaining = self.paisa - other.paisa
        return Currency(0, remaining)