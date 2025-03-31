# Planetary Weights Calculator
# Python 101 - Mini Projects
# Coder: zim

"""
This program asks the user for their name and Earth weight in pounds,
    then calculates and displays their weight on nine celestial bodies
        (Mercury, Venus, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, and Pluto)
            using predefined gravity factors. It uses constants for gravity ratios,
        performs simple multiplication for calculations, and formats
    the output with aligned text and two decimal places via f-strings,
making it come out in a neat and structured manner.
"""

# CONSTANTS: Declare Surface Gravity Factors
nMERCURY_GRAVITY_FACTOR = 0.38
nVENUS_GRAVITY_FACTOR = 0.91
nMOON_GRAVITY_FACTOR = 0.165
nMARS_GRAVITY_FACTOR = 0.38
nJUPITER_GRAVITY_FACTOR = 2.34
nSATURN_GRAVITY_FACTOR = 0.93
nURANUS_GRAVITY_FACTOR = 0.92
nNEPTUNE_GRAVITY_FACTOR = 1.12
nPLUTO_GRAVITY_FACTOR = 0.066

# INPUT: Greet the user and prompt them for their name and Earth weight
sUserName = input("Yet another comes to us for answers...tell us your name, Earthling: ")
fPounds = float(input(f"\nGreetings, {sUserName}! Please enter your Earth weight in pounds(lbs): "))

# PROCESS: Calculate weight on each celestial body in Solar System
fWeightMercury = fPounds * nMERCURY_GRAVITY_FACTOR
fWeightVenus = fPounds * nVENUS_GRAVITY_FACTOR
fWeightMoon = fPounds * nMOON_GRAVITY_FACTOR
fWeightMars = fPounds * nMARS_GRAVITY_FACTOR
fWeightJupiter = fPounds * nJUPITER_GRAVITY_FACTOR
fWeightSaturn = fPounds * nSATURN_GRAVITY_FACTOR
fWeightUranus = fPounds * nURANUS_GRAVITY_FACTOR
fWeightNeptune = fPounds * nNEPTUNE_GRAVITY_FACTOR
fWeightPluto = fPounds * nPLUTO_GRAVITY_FACTOR


# OUTPUT: Display the results for the user, with a humorous closing message
print(f"Here is your weight on each of your Solar System's celestial bodies, {sUserName}: \n")
print(f"{'Mercury weight:':25s} {fWeightMercury:10,.2f}")
print(f"{'Venus weight:':25s} {fWeightVenus:10,.2f}")
print(f"{'Moon weight:':25s} {fWeightMoon:10,.2f}")
print(f"{'Mars weight:':25s} {fWeightMars:10,.2f}")
print(f"{'Jupiter weight:':25s} {fWeightJupiter:10,.2f}")
print(f"{'Saturn weight:':25s} {fWeightSaturn:10,.2f}")
print(f"{'Uranus weight:':25s} {fWeightUranus:10,.2f}")
print(f"{'Neptune weight:':25s} {fWeightNeptune:10,.2f}")
print(f"{'Pluto weight:':25s} {fWeightPluto:10,.2f}")

# -Step 6: Complete program with some sort of ending
print("\nQuite fascinating, is it not?! Now, unless you have some food...be gone!")



