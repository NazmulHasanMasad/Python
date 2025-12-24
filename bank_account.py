#account class with two attribute-Balance and account no.
#methods for debit credit and printing the balance.
class Bank_account():
    def __init__(self, bal, acc):
        self.balance=bal
        self.account=acc

    def debit(self, amount):
        self.balance-=amount
        print("$",amount, "debited")
        print("$", "Total balance :", self.get_balance())

    def credit(self, amount):
        self.balance+=amount
        print("$",amount, "credited")
        print("$", "Total balance :", self.get_balance())

    def get_balance(self):
        return self.balance



c1=Bank_account(10000,12345)
print(c1.balance)
c1.credit(10000)
c1.debit(5000)