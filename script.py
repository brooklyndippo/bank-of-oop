class BankAccount:
    def __init__(self, full_name, account_number, account_type, balance):
        self.name = full_name
        self.account = account_number
        self.type = account_type
        self.balance = balance

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
        print(f'Hello, {self.name}!') 
        print('Your current balance is: ${:0.2f}'.format(self.balance)) 
        return self.balance

    def add_interest(self):
        #if it's a savings account, accrue 1% interest per month
        if self.type == 'savings':
            interest = self.balance * 0.001
            self.balance += interest
        #if it's not a savings account, accrue .083% interest per month
        else:
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

### Test code for each method
print('---------------- Program Test Code ----------------')
print('Test class instance and methods')
print('----------------------------------------------------')
# create an account and test each of the methods
brooklyn = BankAccount('Brooklyn', '227658021', 'savings', 1000.00)
brooklyn.deposit(120)
brooklyn.withdraw(1000)
brooklyn.get_balance()
brooklyn.add_interest()
brooklyn.print_statement()

### Sample Code
print('-------------------- Sample Code --------------------')
print ('Create a bank account for Mitchell')
print('-----------------------------------------------------')

mitchell = BankAccount('Mitchell Hudson', '3141592', 'checking', 0)
mitchell.deposit(400000) #deposit $400,000 into "Mitchell's" account. 
mitchell.print_statement() 
mitchell.add_interest() #add interest to the account
mitchell.print_statement() 
mitchell.withdraw(150) #make a withdraw of $150 for yeezy's 
mitchell.print_statement() 

# stretch challenge 1 - 
# #checking vs savings interest
print('---------------- Stretch Challenge 1 ----------------')
print('See different interest accrual between savings vs. checking accounts')
print('-----------------------------------------------------')

bobs_bank_account = BankAccount ('Bob Bobson', ' 97811764', 'checking', 2500)
bills_bank_account = BankAccount('Bill Billson', '335718401', 'savings', 2500)

bobs_bank_account.add_interest()
bobs_bank_account.print_statement()
bills_bank_account.add_interest()
bills_bank_account.print_statement()

# stretch challenge 2 -
# create a list with all of the bank accounts & add interest to all with for loop
print('---------------- Stretch Challenge 2 ----------------')
print('Add interest to all bank accounts')
print('-----------------------------------------------------')

bank = [brooklyn, mitchell, bobs_bank_account, bills_bank_account]

for account in bank:
    account.add_interest()
    account.print_statement()