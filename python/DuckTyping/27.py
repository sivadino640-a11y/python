class Student:
    def introduce(self):
        print("My name is karthik")
class Employee:
    def introduce(self):
        print("Hi,this is karthik")
def introduce1(obj):
    obj.introduce()
s=Student()
e=Employee()
introduce1(e)
introduce1(s)    