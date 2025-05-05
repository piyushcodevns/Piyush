from person import Person
from bank import BankAccount
from currency import Currency
from digit import Digit

c1 = Currency( 10, 50)
c2 = Currency(5, 75)
p = Person("Piyush", 18, "Varanasi")
b = BankAccount(p, "PNB Piyush National Bank", 12345, 1000) 
digit= Digit(56474)

print(c1,c2)
print(c1+ c2)
