from Account import Account
from BusinessAccount import BusinessAccount
from SavingAccount import SavingAccount

# Testing different accounts and functions

myBusinessAccount = BusinessAccount("Jathon", 100.00)
myBusinessAccount.returnBalance()
myBusinessAccount.increaseBalance(200.00)
myBusinessAccount.returnBalance()

mySavingsAccount = SavingAccount("John", 100.00)
mySavingsAccount.returnBalance()
for i in range(0, 10):
    mySavingsAccount.applyInterest()
mySavingsAccount.returnBalance()

mySavingsAccount.returnAccountName()

print(myBusinessAccount.checksCashed)
myBusinessAccount.addCheck("Costco Check", "Costco", "Jathon", 500)
myBusinessAccount.returnBalance()
myBusinessAccount.cashCheck("Costco Check")