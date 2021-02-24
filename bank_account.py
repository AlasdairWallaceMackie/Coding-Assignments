class Bank_Account:
    def __init__(self, owner_name, interest_rate=.01, balance=0):

        self.owner_name = owner_name
        self.balance = balance
        self.interest_rate = interest_rate

        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent Funds")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        line = "-----------------------------------"
        print(line)
        print(f"{self.owner_name}'s ACCOUNT INFO")
        print(line)
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest_rate}%")
        print(line)
        print("")
        # for attr, value in self.__dict__.items():
        #     print(f"{attr}: {value}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self

    def print_line():
        print("------------")


account1 = Bank_Account("Tommy Brobinski")
account2 = Bank_Account("Stacy Chaddington", 0.79, 100)

account1.deposit(100).deposit(200).deposit(300).withdraw(123).yield_interest().display_account_info()
account2.deposit(1000).deposit(200).withdraw(10).withdraw(20).withdraw(30).withdraw(40).yield_interest().display_account_info()