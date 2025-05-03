from person import Person
from bank import BankAccount

p = Person("Piyush", 18, "Varanasi")
b = BankAccount(p, "PNB Piyush National Bank", 12345, 1000)
print(b)