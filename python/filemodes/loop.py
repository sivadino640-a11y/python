with open("d1.txt","w+") as file:
    file.write("\tkarthik")
    f=file.read()
    print(f)
    for line in file:
        print(line.strip())