class Currency:
    def adjust(self, n):
        if n < 10:
            return "0" + str(n)
        else:
            return str(n)

    def __init__(self, rupees, paisa):
        self.total_paisa = rupees * 100 + paisa

    def __add__(self, other):
        return Currency(0, self.total_paisa + other.total_paisa)

    def __sub__(self, other):
        total_self = self.rupees * 100 + self.paisa
        total_other = other.rupees * 100 + other.paisa
        if total_self < total_other:
            raise ValueError("Insufficient funds!")
        total = total_self - total_other
        return Currency(total // 100, total % 100)

    def __ge__(self, other):
        return (self.rupees, self.paisa) >= (other.rupees, other.paisa)

    def __gt__(self, other):
        return (self.rupees, self.paisa) > (other.rupees, other.paisa)

    def __eq__(self, other):
        return (self.rupees, self.paisa) == (other.rupees, other.paisa)

    def __str__(self):
        rupees = self.total_paisa // 100
        paisa = self.total_paisa % 100
        return f"₹ {self.adjust(rupees)}. {self.adjust(paisa)}"


class BankAccount:
    def __init__(self, customer, bank_name, accountno, balance):
        self.name = customer
        self.bank_name = bank_name
        self.accountno = accountno
        self.balance = balance

    def deposit(self):
        rupees = int(input("Enter deposit rupees: "))
        paisa = int(input("Enter deposit paisa: "))
        amount = Currency(rupees, paisa)
        total_paisa = amount.rupees * 100 + amount.paisa
        if total_paisa > 0:
            self.balance = self.balance + amount
            print("BALANCE UPDATED")
        else:
            print("Deposit amount must be greater than zero.")
    
    def myBalance(self):
        return self.balance

    def withdraw(self):
        rupees = int(input("Enter withdraw rupees: "))
        paisa = int(input("Enter withdraw paisa: "))
        amount = Currency(rupees, paisa)
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("BALANCE UPDATED")
        else:
            print("Insufficient funds! Withdrawal denied.")

    def show_balance(self):
        print(f"Total balance: {self.balance}")

    def detail(self):
        print(f"Account Holder: {self.name}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Number: {self.accountno}")
        print(f"Balance: {self.balance}")

    def __str__(self):
        return f"Account Holder: {self.name}, Bank Name: {self.bank_name}, Account Number: {self.accountno}, Balance: {self.balance}"


if __name__ == "__main__":
    acc = BankAccount("Piyush", "PNB Piyush National Bank", 12345, Currency(0, 0))
    acc = Currency(1, 4)
    print(acc)
    acc = acc + acc
    print(acc)
   