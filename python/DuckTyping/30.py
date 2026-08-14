class Lion:
    def sound(self):
        print("lion sounds")
class Cat:
    def sound(self):
        print("cat sounds")
class Baby:
    def sound(self):
        print("baby sounds")
def sound1(obj):
    obj.sound()
l=Lion()
c=Cat()
b=Baby()
sound1(l)
sound1(c)
sound1(b)

