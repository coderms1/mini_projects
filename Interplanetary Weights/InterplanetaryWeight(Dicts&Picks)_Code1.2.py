# Assignment: Interplanetary Weights w/ Dictionary/Pickling ( improved slightly ;-] )
# Class: Python2 w/ Prof C *
# Author: msimone2301
# Due Date: 10/20/2024

# IMPORT THE PICKLE! (technically step 1?!)
import pickle

# STEP 2: Define the main() function
def main():
    # STEP 3: Create dictionary (key=planet, value=gravity)
    dictPlanetGravity = {
        'Mercury': 0.38,
        'Venus': 0.91,
        'our Moon': 0.165,
        'Mars': 0.38,
        'Jupiter': 2.34,
        'Saturn': 0.93,
        'Uranus': 0.92,
        'Neptune': 1.12,
        'Pluto': 0.066
    }

    # STEP 4: Assign file/initialize dictPlanetHistory
    FILE_NAME = 'msPlanetaryWeights.db'
    dictPlanetHistory = {}

    # STEP 5: TRY to open & read file/EXCEPTion if no history
    try:
        with open(FILE_NAME, 'rb') as file:
            dictPlanetHistory = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print('No history available.')

    # STEP 6: Prompt for user name & validate uniqueness (sName)
    while True:
        sName = input('What is your name (enter key to quit): ').strip().title()
        if not sName:
            break
        if sName in dictPlanetHistory:
            print(f'{sName} is already in the history file. Enter a unique name.')
            continue

        # STEP 7: Prompt user for history -> w/ error handling 
        # (FYI: This part took me the longest to work out. -ms)
        sShowHistory = input('Would you like to see the history? (y/n): ').strip().lower()
        while sShowHistory not in ('y', 'n'):
            print("Invalid entry. Enter 'y' or 'n'.")
            sShowHistory = input('Would you like to see the history? (y/n): ').strip().lower()
        if sShowHistory == 'y':
            print('>> History of Recorded Weights <<')
            for sStoredName, weights in dictPlanetHistory.items():
                print(f">> {sStoredName}'s weights:")
                for sPlanet, fWeight in weights.items():
                    print(f'Weight on {sPlanet:10} {fWeight}')
                print(' - - - - - - - - - - - - - - ')


        # STEP 8: Prompt for weight & validate input
        while True:
            try:
                fEarthWeight = float(input('What is your weight: '))
                break
            except ValueError:
                print('Not valid. Enter your weight as a numeric value.')

        # STEP 9: Calculate weights,store in dictPersonWeights, & display results
        ##> 9.1: Calculate the weight on each planet
        dictPersonWeights = {}
        for sPlanet, fGravityFactor in dictPlanetGravity.items():
            fPlanetWeight = fEarthWeight * fGravityFactor
            dictPersonWeights[sPlanet] = f'{fPlanetWeight:10.2f}'
        
        ##> 9.2: Save to dictPlanetHistory
        dictPlanetHistory[sName] = dictPersonWeights

        ##> 9.3: Display the weights
        print(f"{sName}, here are your weights on our Solar System's planets.")
        for sPlanet, fPlanetWeight in dictPersonWeights.items():
            print(f'Weight on {sPlanet:10} {fPlanetWeight}')

    # STEP 10: Save the pickles and close the file 'jar'
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(dictPlanetHistory, file)
        file.close() 
        print('\nHistory saved.')

# Step 1: Run the main function
main()
