class Account:

    def __init__(self, name: str, password: str, balance: float):

        self.name = name
        self.accountBalance = balance
        self.password = password

    def increaseBalance(self, amount: float, password: str):
        if (self.verifyPassword(password)):
            self.accountBalance += amount
        else:
            print("Wrong Password!")

    def decreaseBalance(self, amount: float, password: str):
        if (self.verifyPassword(password)):
            self.accountBalance -= amount
            print("Successful!")
        else:
            print("Wrong Password!")

    def returnBalance(self):
        print("Account Balance: " + str(self.accountBalance))


    def returnAccountName(self):
        print(self.name)

    def wireMoneyToAccount(self, sender: Account, receiver: Account, password: str):
        # Do this later, first set up password system for all types of accounts
        pass

    def verifyPassword(self, inputtedPassword: str):
        return inputtedPassword == self.password