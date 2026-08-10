from Account import Account
class SavingsAccount(Account):
    
    def __init__(self, name: str, password: str, balance: float):

        super().__init__(name, password, balance)

    def applyInterest(self):

        self.accountBalance = self.accountBalance * 1.03