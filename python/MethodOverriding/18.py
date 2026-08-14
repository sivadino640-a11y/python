class Student:
    def display(self):
        print("Hi")
class Graduate(Student):
    def display(self):
        print("I am a graduate student")
g=Student()
g.display()