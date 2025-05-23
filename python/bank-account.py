class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def withdraw(self):
        wd = int(input("Withdraw: "))
        if self.balance >= wd:
            self.balance -= wd
        else:
            print("Insufficient balance")

    def deposit(self):
        dep = int(input("Deposit: "))
        self.balance += dep

    def display(self):
        print("Account Number: ", self.accountNumber)
        print("Account Name: ", self.name)
        print(f"Account Balance: $ {self.balance}")

newAccount=BankAccount(1234567890, "Joy", 2700)
newAccount.withdraw()
newAccount.deposit()
newAccount.display()