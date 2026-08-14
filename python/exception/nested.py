try:
    x=int(input("Enter x value"))
    try:
        y=int(input("Enter y value"))
        r=x/y
        print(r)
    except ValueError:
        print("error")
except ZeroDivisionError as e:
    print("error",e)