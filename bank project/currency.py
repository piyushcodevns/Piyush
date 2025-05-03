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


class BankAccount:
    def __init__(self, customer, bank_name, accountno, balance=None):
        self.customer = customer
        self.bank_name = bank_name
        self.accountno = accountno
        self.balance = balance or Currency(0, 0)

    def deposit(self, rupees, paisa):
        self.balance = self.balance.add(Currency(rupees, paisa))

    def withdraw(self, rupees, paisa):
        self.balance = self.balance.subtract(Currency(rupees, paisa))

    def detail(self):
        return f"Account Holder: {self.customer}, Bank Name: {self.bank_name}, Account Number: {self.accountno}, Balance: {self.balance}"

    def __str__(self):
        return self.detail()