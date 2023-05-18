atm = {
    'balance': 50,
    'transactions': []
}
def check_balance():
    print("Your current balance is: ${}".format(atm['balance']))

def deposit_money(var1):
    atm['balance'] += var1
    atm['transactions'].append(('deposit', var1))
    print("${} has been deposited to your account.".format(var1))

def withdraw_money(var2):
    if var2 > atm['balance']:
        print("Insufficient funds.")
    else:
        atm['balance'] -= var2
        atm['transactions'].append(('withdraw', var2))
        print("${} has been withdrawn from your account.".format(var2))

def transaction_history():
    print("Transaction History:")
    for transaction in atm['transactions']:
        print("{}: ${}".format(transaction[0], transaction[1]))

while True:
    print("\nWelcome to the ATM Machine\n")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        check_balance()
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        deposit_money(amount)
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        withdraw_money(amount)
    elif choice == '4':
        transaction_history()
    elif choice == '5':
        print("\nThank you for using the ATM Machine. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
