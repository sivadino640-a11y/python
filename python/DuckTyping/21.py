class Duck:
    def talk(self):
        print("Quack")
class Person:
    def talk(self):
        print("Hello")
def make_talk(obj):
        obj.talk()
d=Duck()
p=Person()
make_talk(d)
make_talk(p)



    