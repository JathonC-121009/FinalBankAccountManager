from Account import Account
from SavingsAccount import SavingsAccount
from BusinessAccount import BusinessAccount

class Worker:
    def __init__(self, name: str, bankSystem: "BankingSystem"):
        self.workerName = name
        self.workerBankSystem = bankSystem

    def introduction(self):
        while True:
            print("Welcome to " + self.workerBankSystem.name + " Bank!")
            print("My name is " + self.workerName)
            print("What would you like to do:")
            print("[A] Create an account")
            print("[B] Cash a business check")
            print("[C] Withdraw money")
            print("[D] Display balance")
            print("[E] Exit")
            userInput = input("Action: ")

            if userInput == "A":
                userAccountTypeInput = input("Account type: ")
                userNameInput = input("Name: ")
                userPasswordInput = input("Set a password: ")

                if userAccountTypeInput == "savings":
                    self.workerBankSystem.createAccount(userAccountTypeInput, userNameInput, userPasswordInput, 0.0)
                    print("Savings Account Created")
                elif userAccountTypeInput == "business":
                    self.workerBankSystem.createAccount(userAccountTypeInput, userNameInput, userPasswordInput, 0.0)
                    print("Business Account Created")
                else:
                    print("Not a valid account type!")

            elif userInput == "B":
                userBusinessAccount = input("Name of business account: ")
                # there might be a problem with the if loop under
                for accounts in self.workerBankSystem.accounts:
                    if accounts.name == userBusinessAccount:
                        userBusinessAccountPassword = input("Password: ")

                        if userBusinessAccountPassword == accounts.password:
                            userCheckName = input("Check name: ")
                            userCheckSender = input("Check sender: ")
                            userCheckReceiver = input("Check receiver: ")
                            userCheckAmount = input("Check amount: ")

                            accounts.addCheck(userCheckName, userCheckSender, userCheckReceiver, float(userCheckAmount), userBusinessAccountPassword)
                            print("Done!")
                            continue
                        else:
                            print("Wrong password!")   

                print("Not a valid account!")                                         
            elif userInput == "C":
                userAccount = input("Name of account: ")

                for accounts in self.workerBankSystem.accounts:
                    if userAccount == accounts.name:
                        userWithdrawAmount = input("Amount: ")
                        userAccountPassword = input("Password: ")

                        accounts.decreaseBalance(userWithdrawAmount, userAccountPassword)
                        continue
                print("Not a valid account!")
            elif userInput == "D":
                userAccount = input("Name of account: ")

                for accounts in self.workerBankSystem.accounts:
                    if userAccount == accounts.name:
                        userAccountPassword = input("Password: ")

                        if userAccountPassword == accounts.password:
                            accounts.returnBalance()
                            continue
                        else:
                            print("Wrong password!")
                            continue

                print("Not a valid account!")
            elif userInput == "E":
                break
            else:
                print("That is not a valid action!")