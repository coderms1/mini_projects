# MINI BANKING SYSTEM ~ Capstone Project*
# Coder: zim

################################################################################
#  This program runs a simple little banking system with a menu that lets     ##
#    you do all the basics.  You can deposit, withdraw, check your balance,   ##
#     apply monthly interest, & even save your transaction history to a file. ##
#    Everything’s tracked in a list, fully validated, & printed out nice and  ##
#  clean. It keeps things simple, organized, & works almost like a real ATM!  ##
################################################################################

# FORMAT CURRENCY Function
def format_currency(amount):
    return f"{amount:>13,.2f}"

# PROMPT FOR INPUT Function
def prompt_for_input(sPrompt):
    while True:
        try:
            fAmount = float(input(sPrompt))
            if fAmount > 0:
                return fAmount
            else:
                print("Enter a number that is > 0")
        except ValueError:
            print("Enter a valid number.")

# DEPOSIT Function
def deposit(balance, transactions):
    fAmount = prompt_for_input("Enter deposit amount: ")
    balance += fAmount
    transactions.append(("Deposited:", fAmount))
    print(f"Deposit successful! New balance: ${format_currency(balance)}\n")
    return balance, transactions

# WITHDRAW Function
def withdraw(balance, transactions):
    fAmount = prompt_for_input("Enter withdrawal amount: ")
    if fAmount > balance:
        print("Insufficient Funds.\n")
    else:
        balance -= fAmount
        transactions.append(("Withdrew:", fAmount))
        print(f"Withdrawal successful! New balance: ${format_currency(balance)}\n")
    return balance, transactions

# CHECK BALANCE Function
def check_balance(balance):
    print(f"Your current balance is: ${format_currency(balance)}\n")

# VIEW TRANSACTION Function
def view_transaction_history(transactions):
    print("\nTransaction History:")
    print("+----------------------+----------------+")
    if not transactions:
        print("| No transactions yet.                |")
    else:
        for sType, fAmt in transactions:
            print(f"| {sType:<20} ${format_currency(fAmt)} |")
    print("+----------------------+----------------+\n")

# APPLY INTEREST Function
def apply_interest(balance, transactions):
    if balance == 0:
        print("Balance is $0.00 — no interest will be applied.\n")
        return balance, transactions
    fRate = prompt_for_input("Enter interest rate: ")
    fInterest = balance * (fRate / 100) / 12
    balance += fInterest
    transactions.append(("Interest:", fInterest))
    print(f"Interest has been applied: ${format_currency(fInterest)} New balance: ${format_currency(balance)}\n")
    return balance, transactions

# SAVE TO FILE Function
def save_to_file(balance, transactions):
    sFileName = "BankStatement.txt"
    box_width = 43

    with open(sFileName, "w") as f:
        f.write("+" + "-" * (box_width - 2) + "+\n")
        f.write(f"| {'Zim`s Mini Bank':^{box_width - 2}} |\n")
        f.write(f"| {'Transaction History':^{box_width - 2}} |\n")
        f.write("+" + "-" * (box_width - 2) + "+\n")

        if not transactions:
            f.write(f"| {'No transactions yet.':<{box_width - 2}} |\n")
        else:
            for sType, fAmt in transactions:
                formatted_amt = format_currency(fAmt)
                f.write(f"| {sType:<20} ${formatted_amt:>16} |\n")

        f.write(f"|{'':<{box_width - 2}}|\n")
        f.write(f"| Ending Balance:      ${format_currency(balance):>16} |\n")
        f.write(f"| Transactions Total:  {len(transactions):>16} |\n")
        f.write("+" + "-" * (box_width - 2) + "+\n")

    print(f"Transaction history saved to {sFileName}\n")

# MAIN Function
def main():
    print("Welcome to Zim's Mini-Bank")

    balance = 0.0
    transactions = []

    while True:
        print("""
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. View Transaction History
5. Apply Interest Calculation
6. Save Transaction History to a File
7. Exit
""")
        try:
            iChoice = int(input("Choose an option (1–7): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.\n")
            continue

        if iChoice == 1:
            balance, transactions = deposit(balance, transactions)
        elif iChoice == 2:
            balance, transactions = withdraw(balance, transactions)
        elif iChoice == 3:
            check_balance(balance)
        elif iChoice == 4:
            view_transaction_history(transactions)
        elif iChoice == 5:
            balance, transactions = apply_interest(balance, transactions)
        elif iChoice == 6:
            save_to_file(balance, transactions)
        elif iChoice == 7:
            print("Thanks for using the Mini Bank! Bank statement generated.\nGoodbye!")
            break
        else:
            print("Invalid option. Please select from the menu.\n")

# Call main() funkytown
if __name__ == "__main__":
    main()