class Laptop:
    def power(self):
        print("laptop is power on")
class Desktop:
    def power(self):
        print("desktop is power on")
def power1(obj):
    obj.power()
l=Laptop()
d=Desktop()
power1(l)
power1(d)
