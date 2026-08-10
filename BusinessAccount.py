from Account import Account

class BusinessAccount(Account):

    def __init__(self, name: str, password: str, balance: float, dailyWireLimit: float):

        super().__init__(name, password, balance)
        self.EIN = ""
        self.checksCashed = []
        self.dailyWireLimit = dailyWireLimit
        self.moneyAddedToAccountToday = 0.0

    def setEIN(self, EIN: str):

        self.EIN = EIN

    def addCheck(self, checkName: str, sender: str, receiver: str, amount: float, password: str):

        if receiver == self.name:
            if self.moneyAddedToAccountToday + amount <= self.dailyWireLimit:
                self.increaseBalance(amount, password)
                self.checksCashed.append(checkName)
                self.moneyAddedToAccountToday += amount
            else:
                print("Wait till tomorrow!")
        else:
            print("This check does not belong to you!")

    def returnChecksCashed(self):

        for checkName in self.checksCashed:
            print(checkName)

    def nextDay(self):
        self.moneyAddedToAccountToday = 0.0

    def returnDailyWireLimit(self):
        print(self.dailyWireLimit)

    def returnMoneyAddedToday(self):
        print(self.moneyAddedToAccountToday)