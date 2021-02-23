class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def display_user_balance(self):
        print(f"{self.name}, Balance: ${self.balance}")
    def transfer_money(self, other_user, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.withdrawal(amount)
        other_user.deposit(amount)
        print(f"Transferred ${amount} from {self.name} to {other_user.name}")


user1 = User("Tom Sawyer")
user2 = User("Billy Bob")
user3 = User("Bobby Jo")

user1.deposit(100)
user1.deposit(200)
user1.deposit(300)
user1.withdrawal(250)
user1.display_user_balance()

user2.deposit(123)
user2.deposit(456)
user2.withdrawal(13)
user2.withdrawal(49)
user2.display_user_balance()

user3.deposit(1000)
user3.withdrawal(400)
user3.withdrawal(100)
user3.withdrawal(50)
user3.display_user_balance()

user1.transfer_money(user3, 100)
user1.display_user_balance()
user3.display_user_balance()