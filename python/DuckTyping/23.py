class Teacher:
    def teach(self):
        print("teaching")
class Youtube:
    def teach(self):
        print("teaching")
def teach1(obj):
    obj.teach()
t=Teacher()
y=Youtube()
teach1(t)
teach1(y)