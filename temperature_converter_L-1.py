# Temperature Converter (Level 1)
# Python 101 - Mini Projects
# Coder: zim

"""
This program prompts the user to input a temperature value and its scale
    (F for Fahrenheit or C for Celsius). It then converts the temperature
        to the opposite scale and displays the result, ensuring
        that the temperature stays within the specified range:
                212°F for Fahrenheit and 100°C for Celsius.
            If input is invalid, the program exits with an error message.
        The program emphasizes conditional logic through the use of
    if/elif/else statements to handle scale and temperature validation.
The output is formatted with f-strings to display neat and exact results.
"""

# f_temp = User-entered temperature (float to allow decimals like 68.5)
f_temp = float(input("Enter a temperature: "))

# s_temp_type = User input for temperature scale (F or C), converted to lowercase for simplicity
s_temp_type = input("Is the temp F for Fahrenheit or C for Celsius? ").lower()

# Check if input is valid (F or C); exit if not
if s_temp_type not in ['f', 'c']:
    print("You must enter a F or C")
    exit()

# Convert Fahrenheit to Celsius if 'f' or 'F'
if s_temp_type == 'f':
    if f_temp > 212:
        print("Temp can not be > 212")
    else:
        # f_celsius = Celsius calculation with proper floating-point precision
        f_celsius = (5.0 / 9) * (f_temp - 32)
        print(f"The Celsius equivalent is: {f_celsius:.1f}")

# Convert Celsius to Fahrenheit if 'c' or 'C'
elif s_temp_type == 'c':
    if f_temp > 100:
        print("Temp can not be > 100")
    else:
        # f_fahrenheit = Fahrenheit calculation with proper floating-point precision
        f_fahrenheit = ((9.0 / 5.0) * f_temp) + 32
        print(f"The Fahrenheit equivalent is: {f_fahrenheit:.1f}")