with open("data.txt","r") as file:
    f=file.read()
with open("d1.txt","r") as file:
    f1=file.read()
with open("merge.txt","w") as file:
    file.write(f)
    file.write("\n")
    file.write(f1)