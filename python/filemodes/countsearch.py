w=input("Enter a word")
with open("data.txt","r") as file:
    f=file.read()
    c=f.count(w)
    print("The word appears of:",c)