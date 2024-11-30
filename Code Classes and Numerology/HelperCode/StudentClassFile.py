# Class File: StudentClassFile.py

class Student: # classes encapsulate data and operations into one

  def __init__(self, sName): # the __init__ automically runs when a new object is created
    self.__sName = sName # __sName is a private variable
    print(5)

  def firstInitial(self, sName): # method to get the first initial of the name
    sFirstInitial = sName[0] # get the first letter of the name
    return sFirstInitial
  
  def getName(self):
    return self.__sName
  
  def setName(self, sName):
    self.__sName = sName