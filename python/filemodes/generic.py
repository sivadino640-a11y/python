try:
    with open("data.txt","r") as file:
        print(file.read())
except Exception:
    print("error")
    