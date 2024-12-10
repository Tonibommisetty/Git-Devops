import os
from customer_account import CustomerAccount
from admin import Admin

accounts_list = []
admins_list = []

class BankSystem(object):
    def generate_management_report(self):
        total_customers = len(self.accounts_list)
        total_balance = sum(account.get_balance() for account in self.accounts_list)
        total_overdraft = sum(abs(account.get_balance()) for account in self.accounts_list if account.is_overdraft_taken())
        total_interest_payable = sum(account.calculate_interest() for account in self.accounts_list)

        print("\nManagement Report:")
        print("===================")
        print(f"Total Customers: {total_customers}")
        print(f"Total Balance in All Accounts: {total_balance:.2f}")
        print(f"Total Interest Payable (1 Year): {total_interest_payable:.2f}")
        print(f"Total Overdraft Taken: {total_overdraft:.2f}")


    def save_customer_data(self, file_name="customer_data.txt"):
        with open(file_name, "w") as file:
            for account in self.accounts_list:
                data = account.get_account_details()
                file.write(f"{data}\n")
        print(f"Customer data saved to {file_name}.")

    def load_customer_data(self, file_name="customer_data.txt"):
        if not os.path.exists(file_name):
            print(f"No file named {file_name} found.")
            return

        with open(file_name, "r") as file:
            self.accounts_list = []
            for line in file:
                data = eval(line.strip())
                account = CustomerAccount(
                    fname=data["First Name"],
                    lname=data["Last Name"],
                    address=data["Address"],
                    account_no=data["Account No"],
                    balance=data["Balance"],
                    account_type=data["Account Type"],
                    interest_rate=data["Interest Rate"],
                    overdraft_limit=data["Overdraft Limit"]
                )
                self.accounts_list.append(account)
        print(f"Customer data loaded from {file_name}.")

    def save_customer_details_to_file(self, directory="CustomerDetails"):
        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        file_path = os.path.join(directory, "customer_details.txt")
        
        with open(file_path, "w") as file:
            file.write("Customer Details:\n")
            file.write("=================\n\n")
            for account in self.accounts_list:
                file.write(f"First Name: {account.get_first_name()}\n")
                file.write(f"Last Name: {account.get_last_name()}\n")
                file.write(f"Account No: {account.get_account_no()}\n")
                file.write("Address:\n")
                for line in account.get_address():
                    file.write(f"    {line}\n")
                file.write(f"Balance: {account.get_balance():.2f}\n")
                file.write("------------------------\n")
        
        print(f"Customer details have been saved to {file_path}.")

    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
    
    def load_bank_data(self):
        
        # create customers
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00)
        self.accounts_list.append(customer_1)
        
        account_no+=1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00)    
        self.accounts_list.append(customer_2)

        account_no+=1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00)
        self.accounts_list.append(customer_3)

        account_no+=1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00)
        self.accounts_list.append(customer_4)
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)


    def search_admins_by_name(self, admin_username):
        #STEP A.2
        found_admin = None 
        for a in self.admins_list: 
                username = a.get_username() 
                if username == admin_username:
                    found_admin = a 
                    break 
        if found_admin == None: 
            print("\n The Admin %s does not exist! Try again...\n" %admin_username) 
        return found_admin 
        pass  
        
    def search_customers_by_name(self, customer_lname):
        #STEP A.3
        found_cust = None 
        for account in self.accounts_list: 
            if account.get_last_name() == customer_lname:
                found_cust = account
                break
        if found_cust is None:
            print(f"\n The customer with last name {customer_lname} does not exist! Try again...\n")
        return found_cust 
        pass

    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        option = int(input ("Choose your option: "))
        return option


    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")

    def delete_customer(self, lname):
        account = next((acc for acc in self.accounts_list if acc.get_last_name() == lname), None)
        if account:
            confirm = input(f"\nCustomer '{lname}' found. Delete? (yes/no): ").strip().lower()
            if confirm == 'yes':
                self.accounts_list.remove(account)
                print(f"Customer '{lname}' has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print(f"\nCustomer with last name '{lname}' does not exist!")


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        #ToDo
        sender_account = None
        receiver_account = None

        for account in self.accounts_list:
            if account.get_last_name() == sender_lname:
                sender_account = account
            if account.get_last_name() == receiver_lname and account.get_account_no() == int(receiver_account_no):
                receiver_account = account
        
        if not sender_account:
            print(f"\n Sender with last name {sender_lname} not found!")
            return
        if not receiver_account:
            print(f"\n Receiver with last name {receiver_lname} and account number {receiver_account_no} not found!")
            return
        
        if sender_account.get_balance() < amount:
            print("\n Insufficient funds in the sender's account!")
            return

        # Perform the transfer
        sender_account.withdraw(amount)
        receiver_account.deposit(amount)

        print(f"\n Successfully transferred {amount:.2f} from {sender_lname} to {receiver_lname}.")
        print(f"Sender's new balance: {sender_account.get_balance():.2f}")
        print(f"Receiver's new balance: {receiver_account.get_balance():.2f}")

        # Check if the sender has sufficient funds
        if sender_account.get_balance() < amount:
            print("\n Insufficient funds in the sender's account!")
            return
        pass

                
    def admin_login(self, username, password):
		#STEP A.1 
        found_admin = self.search_admins_by_name(username) 
        msg = "\n Login failed" 
        if found_admin != None:
                if found_admin.get_password() == password: 
                    msg = "\n Login successful" 
        return msg, found_admin 
        pass

    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations & profile settings")
         print ("3) Delete customer")
         print ("4) Print all customers detail")
         print ("5) Sign out")
         print (" ")
         option = int(input ("Choose your option: "))
         return option


    def print_all_accounts_details(self):
        if not self.accounts_list:
            print("\nNo customer accounts available.\n")
            return

        print("\nAll Customer Details:")
        print("~~~~~~~~~~~~~~~~~~~~~~")
        for i, account in enumerate(self.accounts_list, start=1):
            print(f"\nCustomer {i}:")
            account.print_details()
            print("------------------------")


    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)                    
            elif choice == 2:
                customer_name = input("\n Please input customer surname:\n")
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account is not None:
                    customer_account.run_account_options()
                else:
                    print("\n Unable to find the customer. Please try again.")
                pass

            elif choice == 3:
                customer_lname = input("\nEnter the last name of the customer to delete: ")
                self.delete_customer(customer_lname)
                pass
            
            elif choice == 4:
                    self.print_all_accounts_details()
                    pass
            
            elif choice == 5:
                loop = 0
        print ("\n Exit account operations")


    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")


app = BankSystem()
app.run_main_options()
app.save_customer_details_to_file()
app.save_customer_data()
app.load_customer_data()
app.generate_management_report()