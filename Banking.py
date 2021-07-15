import sys


class Customer:

    def __init__(self, Cust_name, act_no):
        self.name = Cust_name
        self.act_no = act_no
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("RS. ", amount, "has been deposited!")
        print("Total balance= ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("INSUFFICIENT FUND")
            sys.exit()
        else:
            self.balance = self.balance - amount
            print("Remaining balance = ", self.balance)

    def blc(self, amount):
        self.balance = amount
        print(self.balance)


print("WELCOME TO BANKING SERVICE")
name = input("enter your name  ")
acno = input("Enter your account no.  ")

c = Customer(name, acno)

while True:
    print("===============================================================")
    print("PLEASE SELECT ONE OPTION")
    print(" B - BALANCE \n D - DEPOSIT \n W - WITHDRAW \n E - EXIT")
    print("================================================================")
    choice = input("ENTER YOUR CHOICE  ")
    amt1 = c.balance
    if choice == "b" or choice == "B":
        c.blc(amt1)

    elif choice == "d" or choice == "D":
        amt = float(input("Enter amount to deposit :  "))
        c.deposit(amt)

    elif choice == "w" or choice == "W":
        amt = float(input("Enter amount to withdraw:  "))
        c.withdraw(amt)

    elif choice == "e" or choice == "E":
        print("THANKS FOR BANKING")
        sys.exit()

    else:
        print("Enter a valid choice")
