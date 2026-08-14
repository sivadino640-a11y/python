class Shape:
    def area(self):
        print("Areas")
class Rectangle:
    def area(self,l,b):
        print("Area of a rectangle:",l*b)        
class Circle:
    def area(self,PI,r):
        print("Area of a circle:",PI*r*r) 
class Triangle:
    def area(self,b,h):
        print("Area of a triangle:",1/2*b*h) 
r=Rectangle()
c=Circle()
t=Triangle()
r.area(2,3)
c.area(3.14,2)
t.area(5,2)
