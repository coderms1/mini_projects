# File: Numerology1.py
# Coder: zim

class Numerology2:
    def __init__(self, sName: str, sDOB: str) -> None:
        self.Name = sName
        self.DOB = sDOB
        self.validate_dob()
        self.validate_name()

        self.__iLifePathNumber = self.__reduceNum(sum(int(digit) for digit in self._nDOB))
        self.__iBirthdayNumber = self.__reduceNum(sum(int(digit) for digit in self._nDOB[2:4]))
        self.__iAttitudeNumber = self.__reduceNum(sum(int(digit) for digit in self._nDOB[:4]))

        vowels = "AEIOU"
        consonants = "".join(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") - set(vowels))

        self.__iSoulNumber = self.__reduceNum(
            sum(self.charToInt(letter) for letter in self._sName if letter in vowels)
        )
        self.__iPersonalityNumber = self.__reduceNum(
            sum(self.charToInt(letter) for letter in self._sName if letter in consonants)
        )
        self.__iPowerName = self.__reduceNum(self.__iSoulNumber + self.__iPersonalityNumber)

    def validate_dob(self) -> None:
        if not (len(self._nDOB) == 8 and self._nDOB.isdigit()):
            raise ValueError("DOB format must be 'mm-dd-yyyy' or 'mm/dd/yyyy'")

    def validate_name(self) -> None:
        if not self._sName:
            raise ValueError("Name cannot be empty.")

    @property
    def Name(self) -> str:
        return self._sName

    @property
    def DOB(self) -> str:
        return self._sDOB

    @Name.setter
    def Name(self, sName: str) -> None:
        self._sName = sName.upper()

    @DOB.setter
    def DOB(self, sDOB: str) -> None:
        self._sDOB = sDOB.replace("-", "").replace("/", "")
        self._nDOB = self._sDOB

    def charToInt(self, sCharacter: str) -> int:
        if sCharacter.isalpha():
            return (ord(sCharacter.upper()) - 65) % 9 + 1
        return 0

    def __reduceNum(self, iNumber: int) -> int:
        while iNumber > 9:
            iNumber = (iNumber % 10) + (iNumber // 10)
        return iNumber

    # Getters for precomputed values
    def getLifePath(self) -> int:
        return self.__iLifePathNumber

    def getBirthDay(self) -> int:
        return self.__iBirthdayNumber

    def getAttitude(self) -> int:
        return self.__iAttitudeNumber

    def getSoul(self) -> int:
        return self.__iSoulNumber

    def getPersonality(self) -> int:
        return self.__iPersonalityNumber

    def getPowerName(self) -> int:
        return self.__iPowerName

    def __str__(self) -> str:
        return (
            f"Test Name: {self.Name}\n"
            f"Test DOB: {self.DOB[:2]}/{self.DOB[2:4]}/{self.DOB[4:]}\n"
            f"Life Path Number: {self.getLifePath()}\n"
            f"Birth Day Number: {self.getBirthDay()}\n"
            f"Attitude Day Number: {self.getAttitude()}\n"
            f"Soul Number: {self.getSoul()}\n"
            f"Personality Number: {self.getPersonality()}\n"
            f"Power Name Number: {self.getPowerName()}"
        )
    