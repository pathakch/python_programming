class Account:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    def deposit(self, amount):
        if float(amount) > float(0):
            self.balance += amount
            self.transaction_history.append(f"Deposited : {self.balance}")
            return True
        return False
    def withdraw(self, amount):
        if amount>self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn : {amount}")
            return True
        return False
    def check_balance(self):
        return self.balance
    def get_transaction_history(self):
        return self.transaction_history
    
class SavingAccount(Account):
    def __init__(self, account_holder, initial_balance, interest_rate = 0.02):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance*self.interest_rate
        self.deposit(interest)
        self.transaction_history.append(f"Interest Applied : {interest}")

class CheckingAccount(Account):
    def __init__(self, account_holder, initial_balance, overdraft_amount=100):
        super().__init__(account_holder, initial_balance)
        self.overdraft_amount = overdraft_amount
    def withdraw(self,  amount):
        if self.balance+self.overdraft_amount >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn : {amount}")
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_holder, initial_balance, interest_rate=0.02):
        if account_holder in self.accounts:
            print(f"Account {account_holder} Already exist")
            return None
        if account_type == 'saving':
            account = SavingAccount(account_holder, initial_balance, interest_rate)
        elif account_type=='checking':
            account = CheckingAccount(account_holder, initial_balance)
        else:
            print("Invalid Account type")
            return False
        self.accounts[account_holder] = account
        print(f"{account_type.upper()} created for {account_holder} with {initial_balance} amount")
        return account
    def get_account(self, account_holder):
        return self.accounts.get(account_holder, None)
    
def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank")
        print("1. Create saving account")
        print("2. Create checking account")
        print("3. Deposit")
        print("4. withdraw")
        print("5. check balance")
        print("6. View transaction History")
        print("7. Apply interest to saving account")
        print("8. Exit")

        choice = input("Enter your choice : ")

        if choice == '1':
            name = input("Enter account holder name : ")
            initial_balance = float(input("Entyer initial balance : "))
            bank.create_account('saving', name, initial_balance)
        elif choice == '2':
            name = input("Enter Account Holder name : ")
            initial_balance = input("Enter initial balance : ")
            bank.create_account('checking', name, initial_balance)
        elif choice == '3':
            name = input("Enter Account Holder name : ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter amount to deposit : "))
                if account.deposit(amount):
                    print(f"Amount {amount} deposited to account {name}")
                else:
                    print("Invalid deposit amount")
            else:
                print("Account Not Found")
        elif choice == '4':
            name = input("Enter Account holder name : ")
            account = bank.get_account(name)
            if account:
                amount = input("Enter amount to withdraw : ")
                if account.withdraw(amount):
                    print(f"Amount {amount} withdrew from account {name}")
                else:
                    print("Invalid amount")
            else:
                print("Account Not Found")
        elif choice == '5':
            name = input("Enter Account holder name : ")
            account = bank.get_account(name)
            if account:
                balance = account.check_balance()
                print(f"This is balance : {balance}")
            else:
                print("Account Not Found")
        elif choice == '6':
            name = input("Enter account holder name : ")
            account = bank.get_account(name)
            if account:
                print(account.get_transaction_history())
            else:
                print("Account Not Found")
        elif choice == '7':
            name = input("Enter Account Holder name : ") 
            account = bank.get_account(name)
            if account:
                if isinstance(account, SavingAccount):
                    account.apply_interest()
                else:
                    print("Interest can be applied only on saving account")
            else:
                print("Account Not Found")
        elif choice == '8':
            print("Thank you for Using Bank, Goodbye !")
            break
        else:
            print("Invalid choice please try again")

if __name__ == "__main__":
    main()

            

