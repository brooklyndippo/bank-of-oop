class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account = account_number
        self.balance = balance

    def format_nums(self, num):
        two_decimals = str(round(num, 2))
        print(f'two decimals {two_decimals}')
        return two_decimals

    def deposit(self, amount):
        self.balance += amount
        print('Amount deposited: ${:0.2f}'.format(amount))
        print('New balance: ${:0.2f}'.format(self.balance))

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print('Amount withdrawn: ${:0.2f}'.format(amount))
            print('New balance: ${:0.2f}'.format(self.balance))
        else:
            print('Insufficient funds.')
            print('Overdraft fee of $10 deducted from your balance.')
            self.balance -= 10

    def get_balance(self):
        print(f'Good day, {self.name}!') 
        print('Your current balance is: ${:0.2f}'.format(self.balance)) 
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
        print('Balance: ${:0.2f}'.format(self.balance)) 
        print('```')


brooklyn = BankAccount('Brooklyn', '227658021', 1000.00)
brooklyn.deposit(120)
brooklyn.withdraw(1000)
brooklyn.get_balance()
brooklyn.print_statement()
brooklyn.deposit(341.33)