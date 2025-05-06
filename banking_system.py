# MINI BANKING SYSTEM ~ Capstone Project
# Coder: Zim

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
def deposit(balance, txn_list):
    fAmount = prompt_for_input("Enter deposit amount: ")
    balance += fAmount
    txn_list.append(("Deposited:", fAmount))
    print(f"Deposit successful! New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# WITHDRAW Function
def withdraw(balance, txn_list):
    fAmount = prompt_for_input("Enter withdrawal amount: ")
    if fAmount > balance:
        print("Insufficient Funds.\n")
    else:
        balance -= fAmount
        txn_list.append(("Withdrew:", fAmount))
        print(f"Withdrawal successful! New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# CHECK BALANCE Function
def check_balance(balance):
    print(f"Your current balance is: ${format_currency(balance)}\n")

# VIEW TRANSACTION Function
def view_history(txn_list):
    print("\nTransaction History:")
    print("+----------------------+----------------+")
    if not txn_list:
        print(f"| No transactions yet. {' ':*15}|")
    else:
        for sType, fAmt in txn_list:
            print(f"| {sType:<20} ${format_currency(fAmt)} |")
    print("+----------------------+----------------+\n")

# APPLY INTEREST Function
def add_interest(balance, txn_list):
    if balance == 0:
        print("Balance is $0.00 — no interest will be applied.\n")
        return balance, txn_list
    fRate = prompt_for_input("Enter interest rate: ")
    fInterest = balance * (fRate / 100) / 12
    balance += fInterest
    txn_list.append(("Interest:", fInterest))
    print(f"Interest has been applied: ${format_currency(fInterest)} New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# SAVE TO FILE Function
def save_to_file(balance, txn_list):
    sFileName = "BankStatement.txt"
    _BOX_WIDTH_ = 43
    _CONTENT_WIDTH_ = 41

    with open(sFileName, "w") as f:
        # Write header
        f.write("+" + "-" * _CONTENT_WIDTH_ + "+\n")
        f.write(f"| {'Zim`s Mini Bank':^{_CONTENT_WIDTH_}} |\n")
        f.write(f"| {'Transaction History':^{_CONTENT_WIDTH_}} |\n")
        f.write("+" + "-" * _CONTENT_WIDTH_ + "+\n")

        # Write transaction history
        if not txn_list:
            f.write(f"| {'No transactions yet.':<{_CONTENT_WIDTH_}} |\n")
        else:
            for sType, fAmt in txn_list:
                formatted_amt = f"{fAmt:>13,.2f}"
                line = f"| {sType:<20} ${formatted_amt:>19} |"
                f.write(line[:_CONTENT_WIDTH_ + 1] + " |\n")

        # Write out footer info
        f.write(f"| {'':<{_CONTENT_WIDTH_}} |\n")
        formatted_balance = f"{balance:>13,.2f}"
        f.write(f"| {'Ending Balance:':<20} ${formatted_balance:>19} |\n")
        f.write(f"| {'Transactions Total:':<20} {len(txn_list):>19} |\n")
        f.write("+" + "-" * _CONTENT_WIDTH_ + "+\n")

    print(f"Transaction history saved to {sFileName}\n")

# MAIN Function
def main():
    print("Welcome to Zim's Mini-Bank")
    # Begin
    balance = 0.0
    txn_list = []

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

        # ATM Choice menu
        match iChoice:
            case 1:
                balance, txn_list = deposit(balance, txn_list)
            case 2:
                balance, txn_list = withdraw(balance, txn_list)
            case 3:
                check_balance(balance)
            case 4:
                view_history(txn_list)
            case 5:
                balance, txn_list = add_interest(balance, txn_list)
            case 6:
                save_to_file(balance, txn_list)
            case 7:
                print("Thanks for using Zim's Mini Bank! Bank statement generated.\nGoodbye! Come back soon.")
                break
            case _:
                print("Invalid option. Please select from the menu.\n")

# Call main() funkytown
if __name__ == "__main__":
    main()
