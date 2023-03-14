#program to show deposit made and balance
class BankAccount:
    def __init__(self, accountno, balance, first_date, customer_name):
        self.accountno=accountno
        self.balance=balance
        
        self.first_date=first_date
        self.customer_name=customer_name
        
    def deposit(self):
        amount=int(input("Enter the amount of deposit: "))
        return amount
    
    def withdraw(self, amount=45000):
        balance=amount-withdrawal
        if "balance" < "amount":
         print("Your balance is not enough: ")
        else:
         return amount
Bank= BankAccount()
print(Bank.deposit())
print(Bank.withdraw())
#    def withdraw(self):
#             if "balance" < "amount":
#      print("Insufficient amount balance:")
#   else:
#        print("Amount: ", "")
         
#    def balance(self):
#         return balance