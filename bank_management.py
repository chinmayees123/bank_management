import csv
from abc import ABC, abstractmethod
class AccountHolder(ABC):
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    @abstractmethod
    def display(self):
        pass
class BankAccount(AccountHolder):
    def __init__(self, account_no, name, balance):
        super().__init__(name)
        self.__account_no = account_no
        self.__balance = balance
        self.__transactions = []
    def get_account_no(self):
        return self.__account_no
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append("Deposited: " + str(amount))
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append("Withdrawn: " + str(amount))
            print("Money withdrawn successfully.")
        else:
            print("Insufficient balance.")
    def display(self):
        print("\nAccount Number:", self.__account_no)
        print("Name:", self.get_name())
        print("Balance:", self.__balance)
    def show_transactions(self):
        print("\n===== TRANSACTION HISTORY =====")
        if len(self.__transactions) == 0:
            print("No transactions found.")
        else:
            for transaction in self.__transactions:
                print(transaction)
class FileManager:
    def save(self, accounts):
        try:
            with open("accounts.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Account No", "Name", "Balance"])
                for account in accounts:
                    writer.writerow([
                        account.get_account_no(),
                        account.get_name(),
                        account.get_balance()
                    ])
            print("Account data saved successfully.")
        except Exception:
            print("Error while saving data.")
accounts = []
while True:
    print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Save Data")
    print("7. Exit")
    choice = input("Enter choice: ")
    match choice:
        case "1":
            try:
                account_no = input("Enter Account Number: ")
                name = input("Enter Account Holder Name: ")
                balance = float(input("Enter Initial Balance: "))
                account = BankAccount(account_no, name, balance)
                accounts.append(account)
                print("Account created successfully.")
            except ValueError:
                print("Please enter a valid amount.")
        case "2":
            account_no = input("Enter Account Number: ")
            found = False
            for account in accounts:
                if account.get_account_no() == account_no:
                    try:
                        amount = float(input("Enter Deposit Amount: "))
                        if amount > 0:
                            account.deposit(amount)
                            print("Money deposited successfully.")
                        else:
                            print("Amount must be greater than 0.")
                    except ValueError:
                        print("Please enter a valid amount.")
                    found = True
                    break
            if not found:
                print("Account not found.")
        case "3":
            account_no = input("Enter Account Number: ")
            found = False
            for account in accounts:
                if account.get_account_no() == account_no:
                    try:
                        amount = float(input("Enter Withdrawal Amount: "))
                        if amount > 0:
                            account.withdraw(amount)
                        else:
                            print("Amount must be greater than 0.")
                    except ValueError:
                        print("Please enter a valid amount.")
                    found = True
                    break
            if not found:
                print("Account not found.")
        case "4":
            account_no = input("Enter Account Number: ")
            found = False
            for account in accounts:
                if account.get_account_no() == account_no:
                    account.display()
                    found = True
                    break
            if not found:
                print("Account not found.")
        case "5":
            account_no = input("Enter Account Number: ")
            found = False
            for account in accounts:
                if account.get_account_no() == account_no:
                    account.show_transactions()
                    found = True
                    break
            if not found:
                print("Account not found.")
        case "6":
            manager = FileManager()
            manager.save(accounts)
        case "7":
            print("Thank you!")
            break
        case _:
            print("Invalid choice.")