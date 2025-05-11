# Compound Interest Calculator w/ Loops (Level 2)
# PYTHON 101 - Mini Projects
# Coder: sim

"""
This program prompts the user for an original deposit, an interest rate,
    the number of months, and a goal amount. It calculates the compound
        interest monthly and prints the account balance for each month
            over the specified period. Focusing on the use of while-loops
                and try-except blocks to handle invalid user input, it
            repeatedly prompts the user until valid data is entered
        and calculates and prints the number of months needed to
    reach or exceed the goal amount through compound interest.
"""

sNUMERIC_ERROR = 'Input must be a positive numeric value'
sPOSITIVE_ERROR = 'Input must be 0 or greater'

while True:
    try:
        fDeposit = float(input("What is the Original Deposit (positive value): "))
        if fDeposit > 0:
            break
        print(sPOSITIVE_ERROR)
    except ValueError:
        print(sNUMERIC_ERROR)

while True:
    try:
        fRate = float(input("What is the Interest rate (positive value): ")) / 100.00 / 12
        if fRate > 0:
            break
        print(sPOSITIVE_ERROR)
    except ValueError:
        print(sNUMERIC_ERROR)

while True:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths > 0:
            break
        print(sPOSITIVE_ERROR)
    except ValueError:
        print(sNUMERIC_ERROR)

while True:
    try:
        fGoal = float(input("What is the Goal amount (can enter 0 but not negative): "))
        if fGoal >= 0:
            break
        print(sPOSITIVE_ERROR)
    except ValueError:
        print(sNUMERIC_ERROR)

fBalance = fDeposit
for iMonth in range(1, iMonths + 1):
    fBalance += fBalance * fRate
    print(f"Month: {iMonth:<2} Account Balance is: ${fBalance:>,.2f}")


if fGoal > 0.0 and fDeposit <= fGoal:
        iMonth = 0
        while fDeposit < fGoal:
            fDeposit += fDeposit * fRate
            iMonth += 1
        print(f"It will take {iMonth} months to reach your goal of ${fGoal:,.2f}")
