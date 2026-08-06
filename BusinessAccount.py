from Account import Account

class BusinessAccount(Account):

    def __init__(self, name: str, balance: float):

        super().__init__(name, balance, "business")
        self.EIN = ""
        self.checksCashed = []

    def setEIN(self, EIN: str):

        self.EIN = EIN

    def addCheck(self, checkName: str, sender: str, receiver: str, amount: float):

        if receiver == self.name:
            super().increaseBalance(amount)
            self.checksCashed.append(checkName)
        else:
            print("This check does not belong to you!")

    def returnChecksCashed(self):

        for checkName in self.checksCashed:
            print(checkName)