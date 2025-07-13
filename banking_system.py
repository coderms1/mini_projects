# MINI BANKING SYSTEM ~ Capstone Project
# Association: STCC
# Coder: MS1

################################################################################
#  This program runs a simple little banking system with a menu that lets     ##
#    you do all the basics. You can deposit, withdraw, check your balance,    ##
#     apply monthly interest, & even save your transaction history to a file. ##
#    Everything’s tracked in a list, fully validated, & printed out nice and  ##
#  clean. It keeps things simple, organized, & works almost like a real ATM!  ##
################################################################################

# FORMAT CURRENCY Function
## Formats float as currency & makes it pretty (commas & 2 decimal pts)
def format_currency(amount):
    return f"{amount:,.2f}"

# PROMPT FOR INPUT Function
## Screens input, requiring a valid positive float
def prompt_for_input(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("Enter a number that is > 0")
        except ValueError:
            print("Enter a valid number.")

# DEPOSIT Function
## Adds amount to balance and logs deposit
def deposit(balance, txn_list):
    amount = prompt_for_input("Enter deposit amount: ")
    balance += amount
    txn_list.append(("Deposited:", amount))
    print(f"Deposit successful! New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# WITHDRAW Function
## Subtracts amount (if there's enough!) and logs withdrawal
def withdraw(balance, txn_list):
    amount = prompt_for_input("Enter withdrawal amount: ")
    if amount > balance:
        print("Insufficient Funds.\n")
    else:
        balance -= amount
        txn_list.append(("Withdrew:", amount))
        print(f"Withdrawal successful! New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# CHECK BALANCE Function
## Displays a formatted balance
def check_balance(balance):
    print(f"Your current balance is: ${format_currency(balance)}\n")

# VIEW TRANSACTION Function
## Prints all txns (deposits, withdrawals, interest)
def view_history(txn_list):
    print("\nTransaction History:")
    print("+----------------------+----------------")
    if not txn_list:
        print(f"| No transactions yet. {' ':*15}")
    else:
        for txn_type, txn_amount in txn_list:
            print(f"| {txn_type:<20} $ {format_currency(txn_amount)}")
    print("+----------------------+----------------")

# APPLY INTEREST Function
## Using the user-inputted APR/12 this applies monthly interest
def add_interest(balance, txn_list):
    if balance == 0:
        print("Balance is $0.00 — no interest will be applied.\n")
        return balance, txn_list
    rate = prompt_for_input("Enter interest rate: ")
    interest = balance * (rate / 100) / 12
    balance += interest
    txn_list.append(("Interest:", interest))
    print(f"Interest has been applied: ${format_currency(interest)} New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# SAVE TO FILE Function
## Dumps full history to a .txt file
def save_to_file(balance, txn_list):
    file_name = "BankStatement.txt"
    SPACE = 60

    # Calculate total deposited and withdrawn
    ## Using sum() to filter and total the txn list based on txn type 
    total_deposited = sum(amount for txn_type, amount in txn_list if txn_type == "Deposited:")
    total_withdrawn = sum(amount for txn_type, amount in txn_list if txn_type == "Withdrew:")

    with open(file_name, "w") as f:
        f.write(f"{'Sim`s Mini Bank':^{SPACE}}\n")
        f.write(f"{'Transaction History':^{SPACE}}\n")
        f.write("\n")

        if not txn_list:
            f.write(f"{'No transactions yet.':^{SPACE}}\n")
        else:
            for txn_type, txn_amount in txn_list:
                f.write(f"{txn_type:<12} $ {format_currency(txn_amount)}\n")
        f.write("\n")

        ### Boxed summary of txns
        f.write(f"+{'-' * SPACE}+\n")
        f.write(f"| Total Deposited:  $ {format_currency(total_deposited):<{SPACE - 22}}|\n")
        f.write(f"| Total Withdrawn:  $ {format_currency(total_withdrawn):<{SPACE - 22}}|\n")
        f.write(f"| Balance:          $ {format_currency(balance):<{SPACE - 22}}|\n")
        f.write(f"+{'-' * SPACE}+\n")

    print(f"Transaction history saved to {file_name}\n")

# MAIN Function
## Contains menu (options 1-6) & main program loop
def main():
    print("Welcome to Sim's Mini-Bank")
    balance = 0.0
    txn_list = []

    while True:
        print("""
        1. Deposit Money
        2. Withdraw Money
        3. Check Balance
        4. View Transaction History
        5. Apply Interest Calculation
        6. Save Transaction History and Exit
        """)

        try:
            choice = int(input("Choose an option (1–6): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 6.\n")
            continue
        
        ### Using match/case list for menu choices
        match choice:
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
                print("Thanks for using Sim's Mini Bank! \n Your banking statement has been generated." \
                "\n   Please come back soon! Goodbye.✌️")
                break
            case _:
                print("Invalid option. Please select from the menu.\n")

# Call & run the main() funkytown 
if __name__ == "__main__":
    main()