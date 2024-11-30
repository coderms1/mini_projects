from StudentClassFile import Student

def main(): 
  StudentObject = Student("zim") # create a new object of the Student class 

  StudentObject.getName()
  print(StudentObject.getName()) # print the name of the student

  StudentObject.__sName = 'm00nz'
  print(StudentObject.getName()) # print the name of the student

  StudentObject.setName('Timmy')
  print(StudentObject.getName()) # print the name of the student


main()


