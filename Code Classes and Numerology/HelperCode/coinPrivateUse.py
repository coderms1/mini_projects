# Author: Prof C.

# Purpose: Introduction to Python Classes Coin Toss Coded for Reuse and Private

#          Make sure to put the .py files in the SAME directory/folder

import coinPrivate

def main():

    myCoin = coinPrivate.Coin()
    bentleyCoin = coinPrivate.Coin()
    ProfCCoin = coinPrivate.Coin()
    
    print("First time: ", myCoin.get_sideup() )

    for iTimes in range(1, 5):
        myCoin.toss()
        print('myCoin: ', iTimes, " Time: ", myCoin.get_sideup() )

        bentleyCoin.toss()
        bentleyCoin.sideup = "Bentley" # INEFFECTIVE - No Worko
        print('bentleyCoin', iTimes, " Time: ", bentleyCoin.get_sideup() )

        ProfCCoin.toss()
        print('ProfCCoin: ', iTimes, " Time: ", ProfCCoin.get_sideup() )

        print()
    

main()
        
