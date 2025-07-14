# Converts an int into its expanded form as a string, 
# showing non-zero digits multiplied by their 
# place value (e.g., 703 becomes "700 + 3").

def expanded_form(num):
    num_str = str(num)
    parts = []
    for i, n in enumerate(num_str):
        if n != '0':
            val = (int(n) * 10 ** (len(num_str) - i - 1))
            parts.append(str(val))
    return " + ".join(parts)

exp_deez = input("Enter number to expand: ")
print(expanded_form(exp_deez))