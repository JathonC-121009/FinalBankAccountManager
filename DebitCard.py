from CheckingAccount import CheckingAccount

class DebitCard:

    def __init__(self, name: str, account: CheckingAccount):

        self.name = name
        self.connectedAccount = account

    def makePurchase(self, amount: float, password: str):

        self.connectedAccount.decreaseBalance(amount, password)