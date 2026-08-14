def age():
    try:
        age=int(input("Enter age"))
        if age<0:
            print("Negative")
        if age>=18:
            print("eligible")
        else:
            print("invalid")
    except ValueError:
        print("error")

a=age()
print("Age is:",a)