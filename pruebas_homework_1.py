"""
Question 9
"""

def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    lista = lst
    for i in range(0, 24):
        tmp1 = lst[-3:]
        print tmp1
        suma = 0
        for x in tmp1:
            suma = suma + x
        lista.append(suma)
    return lista




sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]


"""
Question 10
"""



print type(3.14159)


class BankAccount:
    def __init__(self, initial_balance):

        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fees_paid = 0


    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance = self.balance + amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance = self.balance - amount
        if self.balance < 0:
            self.balance = self.balance - 5
            self.fees_paid = self.fees_paid + 5


    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees_paid



my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print my_account.get_balance(), my_account.get_fees()

def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60

print clock_helper(90)


a = ' kuhwkghwe'
print a[-1]
print a[len(a) -1]
print a.last()
print a[len(a)]