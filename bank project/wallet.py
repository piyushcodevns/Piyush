import random
from datetime import datetime

class Wallet:
    def __init__(self, balance):
        self.balance = balance
        self.wallet = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        self.notes = {denomination: 0 for denomination in self.wallet}

    def distribute_note(self):
        remaining_balance = self.balance
        for denomination in self.wallet:
            if remaining_balance >= denomination:
                self.notes[denomination] = remaining_balance // denomination
                remaining_balance -= self.notes[denomination] * denomination
        if remaining_balance > 0:
            print(f"Unable to distribute the remaining balance of ₹ {remaining_balance}.")

    def display_notes(self):
        print("Distributed notes:")
        for denomination, count in self.notes.items():
            if count > 0: 
                print(f"₹ {denomination}: {count} notes")

    

class WalletWithDate(Wallet):
    def __init__(self, balance):
        super().__init__(balance)
        self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_wallet_info(self):
        print(f"Wallet created on: {self.date_created}")
        self.display_notes()

balance = int(input("Enter the balance: "))
w = WalletWithDate(balance)
w.distribute_note()
w.display_wallet_info()