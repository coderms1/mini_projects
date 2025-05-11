# Compounding Interest Calculator 📱
# Coder: sim

# INPUT (Prompt user)
f_principle = float(input("Enter the starting principal: "))
f_interest_rate = float(input("Enter the annual interest rate: "))
f_times_per_yr = float(input("How many times per year is the interest compounded? "))
i_total_yrs = int(input("For how many years the account will earn interest? "))

# PROCESS (Calcs)
f_final_value = f_principle * (1 + (f_interest_rate / 100) / f_times_per_yr) ** (f_times_per_yr * i_total_yrs)

# OUTPUT (Display results)
print(f"At the end of {i_total_yrs} years you will have $ {f_final_value:1,.2f}")
