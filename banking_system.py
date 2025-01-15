import random

class BackAccountClass:
    def __init__(self, holder_name,  account_number = random.randint(1000000000, 2999999999), amount = 0, balance = 0, ):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.amount = amount


    def account_details(self):
        print(f'Account Name: {self.holder_name}')
        print(f'Account No.: {self.account_number}')
        print(f'Balance: ${self.balance}')
    def my_balance(self):
        print(f'Balance: ${self.balance}')
        self.instruction()


    def deposit(self):
        print('Deposit')
        self.amount=int(input('Amount: $'))
        self.balance += self.amount
        my_account.instruction()


    def withdraw(self):
        print('Withdraw')
        self.amount=int(input('Amount: $'))
        if self.amount > self.balance:
            print('Insufficient Balance')
            self.instruction()
        else:
            print('Withdrawal successful')
            self.balance -= self.amount
            self.instruction()


    def instruction(self):
        print('Do you want to withdraw, deposit or check balance')
        decision = input('>').lower()
        print('\n')
        if decision == 'withdraw':
            my_account.withdraw()
        elif decision == 'deposit':
            my_account.deposit()
        elif decision == 'balance' or decision == 'check balance':
            my_account.my_balance()
        else:
            print('Please enter a valid syntax')

my_account = BackAccountClass(input('Name: '))
my_account.account_details()
my_account.instruction()
