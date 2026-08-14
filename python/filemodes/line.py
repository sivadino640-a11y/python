with open("data.txt","r") as file:
    f=file.read()
    w=f.split()
    print(len(w))