with open("d1.txt","a+") as file:
    file.write("Revanth")
    file.seek(0)
    print(file.read())