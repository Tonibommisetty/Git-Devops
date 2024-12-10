import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from bank_system import BankSystem
from customer_account import CustomerAccount
from admin import Admin



class BankGUI:
    def __init__(self, root, bank_system):
        self.root = root
        self.bank_system = bank_system
        self.root.title("Python Bank System")
        self.show_main_menu()

    def show_main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main Menu
        tk.Label(self.root, text="Welcome to the Python Bank System", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root, text="Admin Login", command=self.admin_login, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.root.quit, font=("Arial", 14), width=20).pack(pady=10)

    def admin_login(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Login Form
        tk.Label(self.root, text="Admin Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Username", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)

        tk.Label(self.root, text="Password", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        password_entry.pack(pady=5)

        def login_action():
            username = username_entry.get()
            password = password_entry.get()
            msg, admin_obj = self.bank_system.admin_login(username, password)
            if admin_obj:
                messagebox.showinfo("Login", "Login successful!")
                self.show_admin_dashboard(admin_obj)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        tk.Button(self.root, text="Login", command=login_action, font=("Arial", 14), width=15).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_main_menu, font=("Arial", 12)).pack(pady=10)

    def show_admin_dashboard(self, admin_obj):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Admin Dashboard
        tk.Label(self.root, text=f"Welcome, {admin_obj.get_first_name()} {admin_obj.get_last_name()}", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root, text="Transfer Money", command=self.transfer_money, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Customer Operations", command=self.customer_operations, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Delete Customer", command=self.delete_customer, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="View All Customers", command=self.view_all_customers, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Generate Report", command=self.generate_report, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.show_main_menu, font=("Arial", 14), width=20).pack(pady=10)

    def transfer_money(self):
        sender_lname = simpledialog.askstring("Input", "Enter Sender's Last Name:")
        receiver_lname = simpledialog.askstring("Input", "Enter Receiver's Last Name:")
        receiver_account_no = simpledialog.askinteger("Input", "Enter Receiver's Account Number:")
        amount = simpledialog.askfloat("Input", "Enter Transfer Amount:")

        if sender_lname and receiver_lname and receiver_account_no and amount:
            self.bank_system.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)

    def delete_customer(self):
        customer_lname = simpledialog.askstring("Input", "Enter Customer's Last Name to Delete:")
        if customer_lname:
            self.bank_system.delete_customer(customer_lname)

    def view_all_customers(self):
        customer_details = "\n".join([str(account.get_account_details()) for account in self.bank_system.accounts_list])
        if customer_details:
            messagebox.showinfo("Customer Details", customer_details)
        else:
            messagebox.showinfo("Customer Details", "No customers available.")

    def generate_report(self):
        # Use the existing management report method
        self.bank_system.generate_management_report()
        
    def customer_operations(self):
        customer_lname = simpledialog.askstring("Customer Operations", "Enter Customer's Last Name:")
        if not customer_lname:
            messagebox.showerror("Error", "Customer last name is required.")
            return
    
        customer_account = self.bank_system.search_customers_by_name(customer_lname)
        if not customer_account:
            messagebox.showerror("Error", f"Customer with last name '{customer_lname}' not found.")
            return

        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
    
        tk.Label(self.root, text=f"Customer Operations - {customer_account.get_first_name()} {customer_account.get_last_name()}", font=("Arial", 18)).pack(pady=20)

        def deposit_money():
            amount = simpledialog.askfloat("Deposit Money", "Enter deposit amount:")
            if amount and amount > 0:
                customer_account.deposit(amount)
                messagebox.showinfo("Success", f"{amount:.2f} deposited successfully.\nNew balance: {customer_account.get_balance():.2f}")
            else:
                messagebox.showerror("Error", "Invalid deposit amount.")

        def withdraw_money():
            amount = simpledialog.askfloat("Withdraw Money", "Enter withdrawal amount:")
            if amount and amount > 0:
                if customer_account.get_balance() >= amount:
                    customer_account.withdraw(amount)
                    messagebox.showinfo("Success", f"{amount:.2f} withdrawn successfully.\nNew balance: {customer_account.get_balance():.2f}")
                else:
                    messagebox.showerror("Error", "Insufficient balance.")
            else:
                messagebox.showerror("Error", "Invalid withdrawal amount.")
                
        def check_balance():
            balance = customer_account.get_balance()
            messagebox.showinfo("Balance Check", f"Current Balance: {balance:.2f}")

        def show_customer_details():
            details = customer_account.get_account_details()
            messagebox.showinfo("Customer Details", details)


        def update_details():
            new_fname = simpledialog.askstring("Update Details", "Enter new first name (leave blank to skip):")
            new_lname = simpledialog.askstring("Update Details", "Enter new last name (leave blank to skip):")
            new_address = simpledialog.askstring("Update Details", "Enter new address (leave blank to skip):")
    
            if new_fname:
                customer_account.update_first_name(new_fname)
            if new_lname:
                customer_account.update_last_name(new_lname)
            if new_address:
                customer_account.update_address(new_address.splitlines())
    
            messagebox.showinfo("Success", "Customer details updated successfully.")

        def back_to_admin_dashboard():
            self.show_admin_dashboard(self.bank_system.search_admins_by_name(customer_account.get_last_name()))
    
        tk.Button(self.root, text="Deposit Money", command=deposit_money, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Withdraw Money", command=withdraw_money, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Update Details", command=update_details, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Check Balance", command=check_balance, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Show customer details", command=show_customer_details, font=("Arial", 14), width=20).pack(pady=10)
        tk.Button(self.root, text="Back", command=back_to_admin_dashboard, font=("Arial", 14), width=20).pack(pady=10)

    

if __name__ == "__main__":
        root = tk.Tk()
        bank_system = BankSystem()
        app = BankGUI(root, bank_system)
        root.mainloop()

