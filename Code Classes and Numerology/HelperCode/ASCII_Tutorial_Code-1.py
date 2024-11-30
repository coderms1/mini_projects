def convert_char_to_int(sCharacter):
  character_to_number_value = 0

  if sCharacter.isalpha():
    character_to_number_value = ((ord(sCharacter.upper()) - 65) % 9 + 1)
    print(sCharacter, ord(sCharacter), character_to_number_value) 

def reduce_number(iNumber):
  while (len(str(iNumber)) > 1):
    iNumber = (iNumber % 10) + (iNumber // 10)

    print(iNumber)
    return iNumber
  
for sChar in "Matty Sim".upper():
  convert_char_to_int(sChar)

reduce_number(123456789)