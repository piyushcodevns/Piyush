from person import Person


class BankAccount:
    def __init__(self, customer, bank_name, accountno, balance=0):
        self.name = customer
        self.bank_name = "PNB Piyush National Bank"
        self.accountno = accountno
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid amount. please enter 0positive number")
        else:
            self.balance += amount
            print("Updated Balance:", self.balance)

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        elif self.balance >= amount:
            self.balance -= amount
            print("Updated Balance:", self.balance)
        else:
            print("Insufficient balance")

    def detail(self):
        print(f"Account Holder: {self.name}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Number: {self.accountno}")
        print(f"Balance: {self.balance}")

    def __str__(self):
        return f"Account Holder: {self.name}, Bank Name: {self.bank_name}, Account Number: {self.accountno}, Balance: {self.balance}"
