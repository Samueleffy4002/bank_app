import tkinter as tk
from tkinter import messagebox

# Mock database of user accounts
user_accounts = {
    '7511823070': {
        'name': 'Peter Smith',
        'pin': '0330',
        'balance': 10000
    },
    '0703291157': {
        'name': 'John Lawrence',
        'pin': '1234',
        'balance': 8000
    }
}

# Global variables
current_user = None


# Functions
def validate_pin():
    pin = pin_entry.get()

    if current_user['pin'] == pin:
        show_menu()
    else:
        messagebox.showerror('Error', 'Invalid PIN')


def show_menu():
    pin_frame.pack_forget()
    menu_frame.pack()


def show_balance():
    messagebox.showinfo('Balance', f"Your balance is ${current_user['balance']}")


def withdraw():
    amount = float(amount_entry.get())

    if amount <= current_user['balance']:
        current_user['balance'] -= amount
        show_balance()
    else:
        messagebox.showerror('Error', 'Insufficient balance')


def logout():
    menu_frame.pack_forget()
    login_frame.pack()
    pin_entry.delete(0, tk.END)


def login():
    account_number = account_entry.get()

    if account_number in user_accounts:
        global current_user
        current_user = user_accounts[account_number]
        login_frame.pack_forget()
        pin_frame.pack()
    else:
        messagebox.showerror('Error', 'Invalid account number')


# GUI
window = tk.Tk()
window.title('ATM')
window.geometry('300x200')

# Login frame
login_frame = tk.Frame(window)
login_label = tk.Label(login_frame, text='Account Number:')
login_label.pack()
account_entry = tk.Entry(login_frame)
account_entry.pack()
login_button = tk.Button(login_frame, text='Login', command=login)
login_button.pack()
login_frame.pack()

# PIN frame
pin_frame = tk.Frame(window)
pin_label = tk.Label(pin_frame, text='Enter PIN:')
pin_label.pack()
pin_entry = tk.Entry(pin_frame, show='*')
pin_entry.pack()
pin_button = tk.Button(pin_frame, text='Submit', command=validate_pin)
pin_button.pack()

# Menu frame
menu_frame = tk.Frame(window)
balance_button = tk.Button(menu_frame, text='Check Balance', command=show_balance)
balance_button.pack()
withdraw_label = tk.Label(menu_frame, text='Enter amount to withdraw:')
withdraw_label.pack()
amount_entry = tk.Entry(menu_frame)
amount_entry.pack()
withdraw_button = tk.Button(menu_frame, text='Withdraw', command=withdraw)
withdraw_button.pack()
logout_button = tk.Button(menu_frame, text='Logout', command=logout)
logout_button.pack()

window.mainloop()