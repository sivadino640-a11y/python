try:
    n1=int(input("Enter a value"))
    n2=int(input("Enter a value"))
    r=n1/n2
    print(r)
except ValueError as e:
    print("error",e)
except ZeroDivisionError as e:
    print("error",e)
else:
    print("Division result:",r)