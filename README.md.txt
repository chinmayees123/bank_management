# Bank Account Management System

## 1. Project Title
Bank Account Management System

## 2. Project Description
The Bank Account Management System is a simple Python-based application used to manage basic bank account operations.
The system allows the user to:
- Create accounts
- Deposit money
- Withdraw money
- Check account balance
- Maintain transaction history
- Save account data
The project demonstrates important Object-Oriented Programming (OOP) concepts such as classes and objects, encapsulation, inheritance, abstraction, file handling, and exception handling.

## 3. Objectives
The main objectives of this project are:
1. To create and manage bank accounts.
2. To deposit money into an account.
3. To withdraw money from an account.
4. To check the account balance.
5. To maintain transaction history.
6. To save account information into a CSV file.
7. To demonstrate Python OOP concepts.
8. To handle invalid inputs and file errors.

## 4. Technologies Used
- Programming Language: Python
- IDE: Visual Studio Code
- File Format: CSV
- Python Modules:
  - csv
  - abc

## 5. Main Features
### 1. Create Account
The user can create a new account by entering:
- Account Number
- Account Holder Name
- Initial Balance

### 2. Deposit Money
The user can deposit money into an existing bank account.

### 3. Withdraw Money
The user can withdraw money if sufficient balance is available.

### 4. Check Balance
The user can check the current balance of an account.

### 5. Transaction History
The system maintains a record of deposits and withdrawals.

### 6. Save Data
The account information can be saved into an `accounts.csv` file.

## 6. Classes Used
### AccountHolder
- Abstract base class.
- Stores the account holder's name.
- Provides getter and setter methods.
- Contains the abstract `display()` method.

### BankAccount
- Inherits from `AccountHolder`.
- Stores account number and balance.
- Performs deposit and withdrawal operations.
- Maintains transaction history.
- Displays account information.

### FileManager
- Handles file operations.
- Saves account information into a CSV file.

## 7. OOP Concepts Demonstrated
### Classes and Objects
The project uses multiple classes and creates objects to manage bank accounts.

### Encapsulation
Private attributes are used to protect account information.
Examples:
    __name
    __account_no
    __balance
    __transactions
Getter and setter methods are used to access or modify data.

### Inheritance
The `BankAccount` class inherits from the `AccountHolder` class.
    AccountHolder
          |
          ↓
    BankAccount

### Abstraction
`AccountHolder` is an abstract class created using the `abc` module.

### File Handling
Account information is saved in:
    accounts.csv

### Exception Handling
`try-except` is used to handle invalid input and file-related errors.

## 8. Menu Options
    ===== BANK ACCOUNT MANAGEMENT SYSTEM =====
    1. Create Account
    2. Deposit Money
    3. Withdraw Money
    4. Check Balance
    5. Transaction History
    6. Save Data
    7. Exit

## 9. How to Run the Project
### Step 1
Open Visual Studio Code.

### Step 2
Create a folder named:
    Bank Account Management System

### Step 3
Create a Python file named:
    bank_management.py

### Step 4
Copy the Python source code into the file.

### Step 5
Open the VS Code terminal.

### Step 6
Run the program using:
    python bank_management.py

### Step 7
Select the required option from the menu.

## 10. Sample Data
Example account:
    Account Number: 1001
    Account Holder Name: Chinmayee
    Initial Balance: 5000
Example transactions:
    Deposited: 2000
    Withdrawn: 1000
Final balance:
    6000

## 11. Output File
After selecting Save Data, the program creates:
    accounts.csv

Example:
    Account No,Name,Balance
    1001,Chinmayee,6000.0

## 12. Error Handling
The program handles:
- Invalid amounts
- Negative amounts
- Invalid menu choices
- Account numbers that do not exist
- Insufficient balance
- File saving errors

Example:
    Enter Withdrawal Amount: 10000
    Insufficient balance.

## 13. Project Files
    Bank Account Management System/
    |
    ├── bank_management.py
    ├── accounts.csv
    ├── README.md
    |
    └── screenshots/
        ├── create_account.png
        ├── deposit.png
        ├── withdraw.png
        ├── check_balance.png
        ├── transaction_history.png
        └── save_data.png

## 14. Conclusion
The Bank Account Management System is a simple Python application for managing basic bank account operations. It provides features such as account creation, depositing money, withdrawing money, checking balance, and viewing transaction history.
The project demonstrates classes and objects, encapsulation, inheritance, abstraction, file handling, and exception handling.