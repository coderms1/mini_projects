# useClassesAgain

from HelperCode.coin import Coin

results = 0

def main():
  zimsCoin = Coin()

  zimsCoin.sideup = 'bloop'

  zimsCoin.toss() 
  for toss in range(1, 11):
    
    zimsCoin.toss()
    print( f'Toss: {toss}\nResult: {zimsCoin.get_sideup()}' )


main()