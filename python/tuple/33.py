t=int(input("Enter a value"))
l=list(t)
l.append(t)
t=tuple(l)
print("The value is :",t)
print(type(t))

