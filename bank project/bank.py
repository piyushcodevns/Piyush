from person import Person
class BankAccount:
    def __init__(self, customer, bank_name, accountno, balance=0):
        self.customer = customer 
        self.bank_name = bank_name
        self.accountno = accountno
        self.balance = balance

    def detail(self):
        print(f"Account Holder: {self.customer}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Number: {self.accountno}")
        print(f"Balance: {self.balance}")

    def __str__(self):
        return f"Account Holder: {self.customer}, Bank Name: {self.bank_name}, Account Number: {self.accountno}, Balance: {self.balance}"
