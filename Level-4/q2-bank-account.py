class BankAccount:
    def __init__(self, account_name, account_no, balance):
        self.account_name = account_name
        self.account_no = account_no
        self.balance = balance

    def show(self):
        print("Bank Name:", self.account_name)
        print("Account No:", self.account_no)
        print("Account Balance:", self.balance)

    def menu(self):
        choice = int(input("[1] Withdrawal\n[2] Deposit\nEnter your choice: "))
        if choice == 1:
            amount = int(input("Enter Withdrawal Amt: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal Successful")
            else:
                print("Insufficient balance")
        elif choice == 2:
            amount = int(input("Enter Deposit Amt: "))
            self.balance += amount
            print("Deposit Successful")
        else:
            print("Invalid choice")

v1 = BankAccount("State Bank Of India", "59841865xxx99", 10000)
v1.show()
v1.menu()
v1.show()
