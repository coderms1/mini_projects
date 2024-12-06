# Numerology.py
'''This is the first version of the Numerology class.
Completed on 11/17/2024.'''
# Assignment: Numerology (submitted version) - 95/100 (95%)
# Class: Python-2 w/ Prof C *
# Author: Matthew Simone
# Due Date: 11/17/2024

class Numerology:
    # Step 1: Initialize the Numerology object with name and DOB
    def __init__(self, sName: str, sDOB: str) -> None:
        self.Name = sName
        self.DOB = sDOB
        self._dict_characters = {
            ('A', 'J', 'S'): 1, ('B', 'K', 'T'): 2, ('C', 'L', 'U'): 3,
            ('D', 'M', 'V'): 4, ('E', 'N', 'W'): 5, ('F', 'O', 'X'): 6,
            ('G', 'P', 'Y'): 7, ('H', 'Q', 'Z'): 8, ('I', 'R'): 9
        }
        # Validate the name and DOB using validate_functions() -> my own addition ;-)
        self.validate_dob()
        self.validate_name()

    # Step 2: Decorator to reduce a number to a single digit
    def _reduceNumberDecorator(func):
        def wrapper(self):
            result = func(self)
            while result > 9:
                result = sum(int(digit) for digit in str(result))
            return result
        return wrapper

    # Step 3: Define Getters (Properties)
    @property
    def Name(self) -> str:
        return self._sName
    @property
    def DOB(self) -> str:
        return self._sDOB

    # Step 4: Define Setters
    # Format the name and DOB in order to use them in calculations
    @Name.setter
    def Name(self, sName: str) -> None:
        self._sName = sName.upper()
    @DOB.setter
    def DOB(self, sDOB: str) -> None:
        self._sDOB = sDOB.replace("-", "").replace("/", "")
        self._nDOB = self._sDOB

    # Step 5: Validate DOB format
    def validate_dob(self) -> None:
        if not (len(self._nDOB) == 8 and self._nDOB.isdigit()):
            raise ValueError("DOB format must be either 'mm-dd-yyyy' or 'mm/dd/yyyy'")

    # Step 6: Validate name is not empty
    def validate_name(self) -> None:
        if not self._sName:
            raise ValueError("Name cannot be empty.")

    # Step 7: Define Numerology Calculations as methods for each Number
    # Life Path
    @_reduceNumberDecorator
    def _getLifePath(self) -> int:
        return sum(int(char) for char in self._nDOB)
    # Birth Day
    @_reduceNumberDecorator
    def _getBirthDay(self) -> int:
        return sum(int(digit) for digit in self._nDOB[2:4])
    # Attitude
    @_reduceNumberDecorator
    def _getAttitude(self) -> int:
        return sum(int(char) for char in self._nDOB[:4])
    # Soul
    @_reduceNumberDecorator
    def _getSoul(self) -> int:
        vowels = "AEIOU"
        return sum(self._letterToNumber(letter)
            for letter in self._sName
            if letter in vowels)
    # Personality
    @_reduceNumberDecorator
    def _getPersonality(self) -> int:
        vowels = "AEIOU"
        return sum(self._letterToNumber(letter) 
                for letter in self._sName 
                if letter not in vowels)
    # Power Name
    @_reduceNumberDecorator
    def _getPowerNumber(self) -> int:
        return self._getSoul() + self._getPersonality()

    # Step 8: Convert Letters to Numerology Numbers-0 for non-alphabetic characters (i.e. spaces!)
    def _letterToNumber(self, letter: str) -> int:
        for key, value in self._dict_characters.items():
            if letter in key:
                return value
        return 0

    # Step 9: Output the Numerology Results in structured format (thx __str__ method!)
    def __str__(self) -> str:
        return (
            f"Test Name: {self.Name}\n"
            f"Test DOB: {self.DOB[:2]}/{self.DOB[2:4]}/{self.DOB[4:]}\n"
            f"Life Path Number: {self._getLifePath()}\n"
            f"Birth Day Number: {self._getBirthDay()}\n"
            f"Attitude Day Number: {self._getAttitude()}\n"
            f"Soul Number: {self._getSoul()}\n"
            f"Personality Number: {self._getPersonality()}\n"
            f"Power Name Number: {self._getPowerNumber()}"
        )
