from Account import Account
from SavingAccount import SavingAccount
from BusinessAccount import BusinessAccount
from typing import List

class BankingSystem:

    def __init__(self, accounts: List[Account], name: str):

        self.accounts = accounts
        self.name = name

    def displayAccounts(self):

        print("Accounts within " + self.name + " banking system: ")
        for accounts in self.accounts:
            print(account)

    def createAccount(self, desiredAccountType: str, accountName: str, balance: float):

        if desiredAccountType == "saving":
            pass
        elif desiredAccountType == "business":
            pass
        else:
            print("This account type does not exist!")
        

