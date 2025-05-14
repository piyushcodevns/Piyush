from person import Person
class BankAccount:
    def __init__(self, customer, bank_name, accountno,balance):
        self.name = customer
        self.bank_name = "PNB Piyush National Bank"
        self.accountno = accountno
        self.balance = balance
 

    def deposit(self, depositamount):
        if depositamount.paisa > 0:
            self.balance += depositamount
            print("Updated Balance:", self.balance)
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount.paisa > self.balance.paisa:
            print("Insufficient funds! Withdrawal denied.")
        else:
            self.balance -= amount
            print("Updated Balance:", self.balance)

    def detail(self):
        print(f"Account Holder: {self.name}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Number: {self.accountno}")
        print(f"Balance: {self.balance}")

    def __str__(self):
        return f"Account Holder: {self.name}, Bank Name: {self.bank_name}, Account Number: {self.accountno}, Balance: {self.balance}"