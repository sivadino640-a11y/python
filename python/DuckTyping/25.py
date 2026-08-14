class Car:
    def start(self):
        print("car is starting")
class Bike:
    def start(self):
        print("Bike is not starting")
def start1(obj):
    obj.start()
c=Car()
b=Bike()
start1(c)
start1(b)