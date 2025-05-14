from person import Person
from bank import BankAccount
from currency import Currency
c = Currency(10, 50)


p = Person("Piyush", 18, "Varanasi")
b = BankAccount(p, "PNB Piyush National Bank", 12345, c)
print(b)
b.deposit(Currency(24, 50))
b.withdraw(Currency(22, 60))