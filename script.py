class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account_num = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        print(f'Amount deposited: ${amount}.')
        print(f'New balance: ${self.balance}.')

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount}.')
            print(f'New balance: ${self.balance}.')
        else:
            print('Insufficient funds.')
            print('Overdraft fee of $10 deducted from your balance.')
            self.balance -= 10

    def get_balance():
        pass
    def add_interest():
        pass
    def print_statement():
        pass


brooklyn = BankAccount('Brooklyn', '227658021', 1000.00)
brooklyn.deposit(120)
brooklyn.withdraw(1000)