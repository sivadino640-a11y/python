class student:
    def __init__ (self,name,age,course):
     self.name=name
     self.age=age
     self.course=course

    def display(self):
     print(self.name,"",self.age,"",self.course,"")
     d=student("karthik","18","python")
     d.display()