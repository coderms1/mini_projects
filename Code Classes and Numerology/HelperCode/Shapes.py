# Author: Prof C.

# Purpose: Combine the Rectangle and Circle into a Shape Class

import math

class Circle:

    def __init__(self, nDiameter):

        self.__diameter = nDiameter
        
    def getRadius(self):

        return self.__diameter / 2

    def getCircumference(self):

        return self.__diameter * math.pi

    def getArea(self):

        return math.pi * (self.getRadius() ** 2 )

        

# Authors Prof. C 
# Super Fantastic Students

class Rectangle:
    # First part of the code to set up and store
    # and protect/Encapsulate the length and width:
    def __init__(self, nWidth, nLength):
        self.__width = nWidth
        self.__length = nLength

    # Code the "getters":
    def getArea(self):
        return self.__width * self.__length
        
    def getLength(self):
        return self.__length

    def getPerimeter(self):
        return (self.__width * 2) + (self.__length * 2)

    def getWidth(self):
        return self.__width

    # Code the "is-ers":
    def isSquare(self):
        return self.__width == self.__length

    # Code the "setters":
    def setLength(self, NewLength):
        self.__length = NewLength
    
    def setWidth(self, NewWidth):
        self.__width = NewWidth
    
