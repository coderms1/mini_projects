# Assignment: Interplanetary Weights w/ Dictionary/Pickling 
# Class: Python2 w/ Prof C*
# Author: msimone2301
# Due Date: 10/20/2024

# (technically step 1?) IMPORT THE PICKLE!
import pickle

# Define the main function
def main():
    #STEP 2: Establish Weights/Planets (Weights=Key, Planets=Value)
    dictPlanetGravity = {
        'Mercury': 0.38,
        'Venus': 0.91,
        'Moon': 0.165,
        'Mars': 0.38,
        'Jupiter': 2.34,
        'Saturn': 0.93,
        'Uranus': 0.92,
        'Neptune': 1.12,
        'Pluto': 0.066
    }

    #STEP 3: Assign file/dict --> try to open/except if no history
    file_name = "rmPlanetaryWeights.db"
    dictPlanetHistory = {}

    try:
        with open(file_name, 'rb') as file:
            dictPlanetHistory = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print(f"File '{file_name}' not found or empty. Creating a new one.")

    #STEP 4: Prompt to show history and list previous entries
    sShowHistory = input("Would you like to see the history? (Y/N): ").strip().lower()
    if sShowHistory == 'y':
        print()
        print("History of entries:")
        for sName, weights in dictPlanetHistory.items():
            print(f"{sName}:")
            for planet, weight in weights.items():
                print(f"    {planet:10}: {weight} pounds")
        print("-" * 35)

    #STEP 5: While loop for additional input/attempts
    while True:
        sName = input("What is your name (enter key to quit): ").strip().title()
        if not sName:
            break
        if sName in dictPlanetHistory:
            print(f"{sName} is already in the history file. Enter a unique name.")
            continue

        #STEP 5.1: Prompt for Earth weight with exception handling
        while True:
            try:
                fEarthWeight = float(input(f"What is your weight: "))
                break
            except ValueError:
                print("Invalid input, hooman. Please enter a valid number.")

        #STEP 5.2: Calculate and save weights for each planet (saved to dictPersonWeights{})
        dictPersonWeights = {}
        for sPlanet, fGravityFactor in dictPlanetGravity.items():
            fPlanetWeight = fEarthWeight * fGravityFactor
            dictPersonWeights[sPlanet] = f"{fPlanetWeight:10.2f}"

        dictPlanetHistory[sName] = dictPersonWeights

        #STEP 7: Use For Loop to Format and Print Output
        print()
        print(f"{sName}, here are your weights on our Solar System's planets.")
        for sPlanet, fPlanetWeight in dictPersonWeights.items():
            print(f"Weight on {sPlanet:10}: {fPlanetWeight}")

    #STEP 6: Pickle and save the history dictionary
    with open(file_name, 'wb') as file:
        pickle.dump(dictPlanetHistory, file)

#STEP 1: Call main function
main()
