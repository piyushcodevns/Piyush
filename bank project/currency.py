class Currency:
    def __init__(self, rupees, paisa):
        self.paisa = rupees * 100 + paisa

    def __str__(self):
        rs = self.paisa // 100
        ps = self.paisa % 100
        return f"₹ {rs}.{ps}"

    def __add__(self, other):
        paisa = self.paisa + other.paisa
        # rupees = self.rupees + other.rupees + (paisa // 100)
        return Currency(0, paisa)

    def __sub__ (self, other):
        
        remaining = self.paisa - other.paisa
        return Currency(0, remaining)
    
    def __eq__(self, other):
        return self.paisa == other.paisa