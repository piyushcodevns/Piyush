from currency import Currency
from bank import BankAccount

account = BankAccount("Alice", "PNB", "12345", Currency(0, 50))  
try:
    account.deposit(Currency(0, 50)) 
    account.withdraw(Currency(1, 0)) 
except ValueError as e:
    print(e)