from Account import Account
class SavingAccount(Account):
    
    def __init__(self, name: str, balance: float):

        super().__init__(name, balance, "saving")

    def applyInterest(self):

        self.accountBalance = self.accountBalance * 1.03

        

    

    