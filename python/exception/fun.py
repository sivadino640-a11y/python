def divide(x,y):
  try:
    r=x/y
    return r
  except ZeroDivisionError:
     print("error")
x=int(input("enter x value"))
y=int(input("enter y value"))

print(divide(x,y))