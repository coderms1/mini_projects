# Author: Prof C.

# Purpose: Introduction to Python Classes Coin Toss Coded for Reuse and Private

#          Make sure to put the .py files in the SAME directory/folder

import random

class Coin:

    def __init__(self):
# Notice I made the side_up variable PRIVATE
# by adding to underscores in front of the name
#            ||
#            ||
#            VV 
        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0,1) == 0:
# Notice I made the side_up variable PRIVATE
# by adding to underscores in front of the name
#                ||
#                ||
#                VV 
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):

# Notice I made the side_up variable PRIVATE
# by adding to underscores in front of the name
#                   ||
#                   ||
#                   VV 
        return self.__sideup
  

