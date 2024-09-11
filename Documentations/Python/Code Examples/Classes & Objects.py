class Student:
    def __init__(self, name, major, GPA, is_on_propation):
        self.name = name
        self.major = major
        self.GPA = GPA
        self.is_on_propation = is_on_propation
    def Excelent_Student(self):
        if self.GPA >= 3.6:
            return True
        else:
            return False
        

Student1 = Student("Jack", "Engineering", 3.2, False)

print(Student1.GPA)
print(Student1.Excelent_Student())