class Dog:
    def sound(self):
        print("barking")
class RobotDog:
    def sound(self):
        print("barking")
def sound1(obj):
    obj.sound()
d=Dog()
r=RobotDog()
sound1(d)
sound1(r),45891