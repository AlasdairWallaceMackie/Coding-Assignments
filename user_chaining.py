class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return self

    def deposit(self, amount):
        self.balance += amount
        return self

    def display_user_balance(self):
        print(f"{self.name}, Balance: ${self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.withdrawal(amount)
        other_user.deposit(amount)
        print(f"Transferred ${amount} from {self.name} to {other_user.name}")
        return self


user1 = User("Tom Sawyer")
user2 = User("Billy Bob")
user3 = User("Bobby Jo")

user1.deposit(100).deposit(200).deposit(300).withdrawal(250).display_user_balance()

user2.deposit(123).deposit(456).withdrawal(13).withdrawal(49).display_user_balance()

user3.deposit(1000).withdrawal(400).withdrawal(100).withdrawal(50).display_user_balance()

user1.transfer_money(user3, 100).display_user_balance()
user3.display_user_balance()