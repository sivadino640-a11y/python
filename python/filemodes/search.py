word=input("Enter a word:")
with open("data.txt","r") as file:
    f=file.read()
    if word in f:
        print("Found:",word)
    else:
        print("not found",word)