class BankAccount:
    def __init__(self, account_name, account_no, balance):
        self.account_name = account_name
        self.account_no = account_no
        self.balance = balance

    def show(self):
        print("Bank Name:", self.account_name)
        print("Account No:", self.account_no)
        print("Account Balance:", self.balance)

    def aeps(self):
        choice = int(input("[1]: Withdrawal\n[2]: Deposit\nEnter your choice: "))
        if choice == 1:
            amount = int(input("Enter Withdrawal Amt: "))
            if amount <= self.balance:
                self.balance -= amount
                print("-" * 40)
                print("Withdrawal Successful")
                print("-" * 40)
            else:
                print("Insufficient balance")
        elif choice == 2:
            amount = int(input("Enter Deposit Amt: "))
            self.balance += amount
            print("-" * 40)
            print("Deposit Successful")
            print("-" * 40)
        else:
            print("Invalid choice")

v1 = BankAccount("State Bank Of India", "59841865xxx99", 10000)
v1.show()
v1.aeps()
v1.show()
