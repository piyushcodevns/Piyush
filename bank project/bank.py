from person import Person



class BankAccount:
    def __init__(self, customer, bank_name, accountno,balance):
        self.name = customer
        self.bank_name = "PNB Piyush National Bank"
        self.accountno = accountno
        self.balance = balance

    # def deposit(self,depositamount):
    #         self.balance += depositamount
    #         print("Updated Balance:", self.balance)

    # def withdraw(self,amount):
    #         self.balance -= amount

    def validate_balance(self):
         if self.balance < 0:
            raise ValueError("Error: Balance cannot be Zero or Negative")
original_deposit = BankAccount.deposit
def new_deposit(self, depositamount):
    BankAccount.deposit(self, depositamount)
    self.validate_balance()  

original_withdraw = BankAccount.withdraw
def new_withdraw(self, amount):
    BankAccount.withdraw(self, amount)
    self.validate_balance()  

BankAccount.deposit = new_deposit
BankAccount.withdraw = new_withdraw
 
def detail(self):
        print(f"Account Holder: {self.name}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Number: {self.accountno}")
        print(f"Balance: {self.balance}")

def __str__(self):
        return f"Account Holder: {self.name}, Bank Name: {self.bank_name}, Account Number: {self.accountno}, Balance: {self.balance}"