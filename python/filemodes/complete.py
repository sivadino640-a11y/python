try:
    with open("data.txt","r") as file:
        f=file.read()
except FileNotFoundError:
    print("error")
except PermissionError:
    print("error")
else:
    print(f)
finally:
    print("Executed successfully")

    