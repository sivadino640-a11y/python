try:
    age=int(input("Enter a age"))
    if age<18:
        raise ValueError("Age must be in greater than 18")
except ValueError as e:
    print("error",e)
else:
    print("Eligible")