


class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type="Standard", interest_rate=0.01, overdraft_limit=0.0):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.account_type = account_type
        self.interest_rate = float(interest_rate)
        self.overdraft_limit = float(overdraft_limit)
    
    def get_account_details(self):
        return {
            "First Name": self.fname,
            "Last Name": self.lname,
            "Account No": self.account_no,
            "Address": self.address,
            "Balance": self.balance,
            "Account Type": self.account_type,
            "Interest Rate": self.interest_rate,
            "Overdraft Limit": self.overdraft_limit
        }
    
    def is_overdraft_taken(self):
        return self.balance < 0

    def calculate_interest(self):
        return max(0, self.balance) * self.interest_rate

    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):   
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        
    def get_address(self):
        return self.address
    
    def deposit(self, amount):
        self.balance+=amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("\n Withdrawal amount exceeds available balance!")    
        else:
            self.balance -= amount

        print(f"Current Balance of {self.lname} is {self.balance}")
        pass
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" %self.fname) 
        print("Last name: %s" %self.lname) 
        print("Account No: %s" %self.account_no) 
        print("Address: %s" %self.address[0]) 
        print("         %s" %self.address[1]) 
        print("         %s" %self.address[2]) 
        print("         %s" %self.address[3]) 
        print(" ")
        pass
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #STEP A.4.1
                amount=float(input("\n Please enter amount to be deposited: ")) 
                self.deposit(amount) 
                self.print_balance() 
                pass
            elif choice == 2:
                #ToDo
                amount = float(input("\n Please enter the amount to withdraw: "))
                self.withdraw(amount)
                pass
            elif choice == 3:
                #STEP A.4.4
                self.print_balance() 
                pass
            elif choice == 4:
                #STEP A.4.2 
                fname=input("\n Enter new customer first name: ") 
                self.update_first_name(fname) 
                sname = input("\nEnter new customer last name: ") 
                self.update_last_name(sname) 
                pass
            elif choice == 5:
                #ToDo
                address = input("Enter the new customer address :")
                self.address = address
                self.update_address(self.address)
                pass
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                BankSystem().admin_menu()
        print ("\n Exit account operations")