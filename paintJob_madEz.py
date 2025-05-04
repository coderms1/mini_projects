# Paint Job Estimator (Made EZ: Version 3.0)
# Coder: zim

from math import ceil

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Enter a number > 0!")
        except ValueError:
            print("Enter a valid number!")

def main():
    # Tax rates (dictionary)
    tax_rates = {'CT': 0.06, 'VT': 0.06, 'MA': 0.0625, 'ME': 0.085, 'RI': 0.07, 'NH': 0.0}

    # Get inputs
    wall_space = get_float("Wall space (sq ft): ")
    paint_price = get_float("Paint price ($/gal): ")
    feet_per_gallon = get_float("Feet per gallon: ")
    labor_hrs_per_gallon = get_float("Labor hours per gallon: ")
    labor_charge_hr = get_float("Labor charge ($/hr): ")
    state = input("State (CT, VT, MA, ME, RI, NH): ").upper()
    last_name = input("Client's last name: ").strip() or "Unknown"

    # Calculations
    gallons = ceil(wall_space / feet_per_gallon)
    labor_hours = labor_hrs_per_gallon * gallons
    paint_cost = gallons * paint_price
    labor_cost = labor_hours * labor_charge_hr
    tax_rate = tax_rates.get(state, 0.0)
    tax = tax_rate * (paint_cost + labor_cost)
    total_cost = paint_cost + labor_cost + tax

    # Output
    output = (f"Customer: {last_name}\n"
        f"Gallons: {gallons}\n"
        f"Labor Hours: {labor_hours:.2f}\n"
        f"Paint Cost: ${paint_cost:.2f}\n"
        f"Labor Cost: ${labor_cost:.2f}\n"
        f"Tax: ${tax:.2f}\n"
        f"Total: ${total_cost:.2f}")
    print("\nEstimate:\n" + output)

    # Save to file
    filename = f"{last_name}_PaintJobOutput.txt"
    with open(filename, "w") as file:
        file.write(output)
    print(f"File '{filename}' created.")

main()