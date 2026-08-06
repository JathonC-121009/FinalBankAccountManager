class Account:

    def __init__(self, name: str, balance: float, ownerType: str):

        self.name = name
        self.accountBalance = balance
        self.ownerType = ownerType

    def increaseBalance(self, amount: float):

        self.accountBalance += amount

    def decreaseBalance(self, amount: float):

        self.accountBalance -= amount

    def returnBalance(self):

        print("Account Balance: " + str(self.accountBalance))

    def returnAccountName(self):

        print(self.name)