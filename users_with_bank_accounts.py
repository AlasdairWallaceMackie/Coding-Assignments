class Bank_Account:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def yield_interest(self):
        self.balance += ( self.balance * self.interest_rate )
        return self

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.accounts = {
            "Checking": Bank_Account(balance=0, interest_rate=0.02)
        }
        
##########################################################
##########################################################

    def deposit(self, nickname, amount):
        nickname = self.format_nickname(nickname)
        if nickname != False:
            self.accounts[nickname].balance += amount
        return self

    def withdraw(self, nickname, amount):
        nickname = self.format_nickname(nickname)
        if nickname != False:
            if amount > self.accounts[nickname].balance:
                print("Insufficient Funds")
            else:
                self.accounts[nickname].balance -= amount
        return self

    def internal_transfer(self, origin_nickname, destination_nickname, amount):
        origin_nickname = self.format_nickname(origin_nickname)
        destination_nickname = self.format_nickname(destination_nickname)
        if origin_nickname != False and destination_nickname !=False:
            if amount > self.accounts[origin_nickname].balance:
                print("Insufficient Funds")
            else:
                self.accounts[origin_nickname].balance -= amount
                self.accounts[destination_nickname].balance += amount
        return self

    def external_transfer(self, origin_nickname, other_user, other_user_account_nickname, amount):
        origin_nickname = self.format_nickname(origin_nickname)
        other_user_account_nickname = self.format_nickname(other_user_account_nickname)

        if origin_nickname != False and other_user_account_nickname != False:
            if amount > self.accounts[origin_nickname].balance:
                print("Insufficient Funds")
            else:
                self.accounts[origin_nickname].balance -= amount
                other_user.accounts[other_user_account_nickname].balance += amount
        return self

####################################################

    def create_account(self, nickname):
        if nickname == None:
            print("Please give a nickname for this account")
        else:
            nickname = nickname.casefold().capitalize()
            self.accounts[nickname] = Bank_Account(balance=0, interest_rate=0.02)
        return self

    def display_account_info(self):
        line = "-----------------------------------"
        print(line)
        print(f"{self.first_name} {self.last_name}'s ACCOUNT INFO")
        print(line)
        for account in self.accounts:
            print("____________")
            print(f"{account}")
            print("------------")
            print(f"Balance: ${self.accounts[account].balance}")
            print(f"Interest Rate: {self.accounts[account].interest_rate}%")
            print(line)
        print("")
        return self

########################################################        

    def format_nickname(self, nickname):
        if nickname == None:
            print("Please specify an account")
            return False
        else:
            return nickname.casefold().capitalize()

user1 = User('Fist', 'Thunderballs', 'fthunderballs@xcom.gov').create_account("sAvInGs").create_account("investing")
user1.deposit('Checking', 1000).deposit('Savings', 10000).internal_transfer('Savings', 'Investing', 500)

user2 = User('Fabio', 'Ravioli', 'mrravioli@vatican.it').create_account('Vacation Fund').deposit('Vacation Fund', 1000).withdraw('Vacation Fund', 25)
user1.external_transfer('checking', user2, 'cHECKing', 250)

user1.display_account_info()
user2.display_account_info()