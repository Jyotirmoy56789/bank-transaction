class Bank:
    
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount
        
    def log_transaction(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\tbalance: {self.balance}\n")
        
    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"withdrew {amount}")
    
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"deposited {amount}")
account = Bank(50.50)
while True:
    try:
        action = input("action : ")
    except KeyboardInterrupt:
        print(" leaving ATM")
        break
    if action in ["withdrawal","deposit"]:
        if action == "withdrawal":
            amount = input("\nhow much you want to withdraw :")
            account.withdrawal(amount)
            
        else:
            amount = input("\nhow much you want to deposit :")
            account.deposit(amount)
            
        print("\nyour balance is", account.balance)
    
    else:
        print("\nnot a valid action, try again")