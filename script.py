class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account = account_number
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

    def get_balance(self):
        print(f'Good day, {self.name}!') 
        print(f'Your current balance for account number {self.account} is: ${self.balance}') 
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        #create a string with asterisks to represent hidden digits
        hidden_digits = (len(self.account) - 4) * '*'
        #get the last four numbers of the account number to display
        last_four = self.account[-4:]
        print('```')
        print(f'{self.name}') 
        print(f'Account No.: {hidden_digits}{last_four}') 
        print(f'Balance: ${self.balance}') 
        print('```')


brooklyn = BankAccount('Brooklyn', '227658021', 1000.00)
brooklyn.deposit(120)
brooklyn.withdraw(1000)
brooklyn.get_balance()
brooklyn.print_statement()