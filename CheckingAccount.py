from DebitCard import DebitCard

class CheckingAccount:

    def __init__(self, name: str, password: str, balance: float):

        super().__init__(name, password, balance)
        self.debitCard = None

    def createDebitCard(self, name: str):

        self.debitCard = DebitCard(name, self)