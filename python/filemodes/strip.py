with open("data.txt","r+") as file:
    file.write("karthik")
    for line in file:
        print(line.strip())