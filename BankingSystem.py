from Account import Account
from SavingsAccount import SavingsAccount
from BusinessAccount import BusinessAccount
from typing import List
from Worker import Worker

class BankingSystem:

    def __init__(self, accounts: List[Account], workers: List[Worker], name: str):

        self.accounts = accounts
        self.name = name
        self.workers = workers

    def displayAccounts(self):

        print("Accounts within " + self.name + " banking system: ")
        for accounts in self.accounts:
            accounts.returnAccountName()

    def createAccount(self, desiredAccountType: str, accountName: str, accountPassword: str, balance: float):

        if desiredAccountType == "savings":
            newAccount = SavingsAccount(accountName, accountPassword, balance)
            self.accounts.append(newAccount)
        elif desiredAccountType == "business":
            newAccount = BusinessAccount(accountName, accountPassword, balance, 1000.00)
            self.accounts.append(newAccount)
        else:
            print("This account type does not exist!")

    def hireWorker(self, name: str):

        newWorker = Worker(name, self)
        self.workers.append(newWorker)

    def displayWorkers(self):

        for worker in self.workers:
            print(worker.workerName)

    def fireWorker(self, workerName: str):

        for worker in self.workers:
            if worker.workerName == workerName:
                self.workers.remove(worker)

    def talkToWorker(self, workerName: str):

        for worker in self.workers:
            if worker.workerName == workerName:
                worker.introduction()