# Assignment: Interplanetary Weights w/ Dictionary/Pickling 
# Class: Python2 w/ Prof C *
# Author: Matthew Simone
# Due Date: 10/20/2024

# (technically STEP 1?) --> IMPORT THE PICKLE!
import pickle

# Define the main function
def main():
    # STEP 2: Establish Weights/Planets (Weights=Key, Planets=Value)
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

    # STEP 3: Assign file/dict 
    file_name = 'rmPlanetaryWeights.db'
    dictHistOfPlanet = {}

    # STEP 3.1: Try to open/except if no history
    try:
        with open(file_name, 'rb') as file:
            dictHistOfPlanet = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print(f"File '{file_name}' not found, no history available.")

    # STEP 5: Start by asking for the NAME
    while True:
        sName = input('What is your name (enter key to quit): ').strip().title()
        if not sName:
            break
        if sName in dictHistOfPlanet:
            print(f'{sName} is already in the history file. Enter a unique name.')
            continue

        # STEP 4: Ask to show history ~ list previous entries
        sShowHistory = input('Would you like to see the history? y/n: ').strip().lower()
        if sShowHistory == 'y':
            print('History of recorded weights:')
            for sStoredName, weights in dictHistOfPlanet.items():
                print('---- ' * 5)
                print(f'{sStoredName}:')
                for planet, weight in weights.items():
                    print(f'{planet:10} {weight}')
            print('---- ' * 5)

        # STEP 5.1: While/true for input & exception handling
        while True:
            try:
                fEarthWeight = float(input('What is your weight: '))
                break
            except ValueError:
                print('Not valid. Enter your weight: ')

        # STEP 5.2: Calculate and save weights for each planet (saved to dictWeightEntries{})
        dictWeightEntries = {}
        for sPlanet, fGravityFactor in dictPlanetGravity.items():
            fPlanetWeight = fEarthWeight * fGravityFactor
            dictWeightEntries[sPlanet] = f'{fPlanetWeight:10.2f}' #Prof C showed us this trick ;)

        # STEP 5.3: Add to the history dict
        dictHistOfPlanet[sName] = dictWeightEntries

        # STEP 7: For Loop to format & print OUTPUT
        print(f"\n{sName}, here are your weights on our Solar System's planets.")
        for sPlanet, fPlanetWeight in dictWeightEntries.items():
            print(f'{sPlanet:10} {float(fPlanetWeight):10.2f}')

    # STEP 6: Pickle and store data
    with open(file_name, 'wb') as file:
        pickle.dump(dictHistOfPlanet, file)
        print('\nHistory saved.')

# STEP 1: Call the main function to run it!
main()