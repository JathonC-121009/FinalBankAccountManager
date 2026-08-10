from Account import Account
from BusinessAccount import BusinessAccount
from SavingsAccount import SavingsAccount
from BankingSystem import BankingSystem

# Testing different accounts and functions

myBankingSystem = BankingSystem([], [], "Jathon's Bank")

myBankingSystem.hireWorker("Joe")
myBankingSystem.hireWorker("Bob")
myBankingSystem.hireWorker("Sally")

myBankingSystem.talkToWorker("Joe")