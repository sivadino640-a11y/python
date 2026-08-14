with open("data.txt","r") as file:
 f=file.read()
 w=f.split()
 print("words lenght:",len(w))
 print("character:",len(f))
 print("lines count:",len(f))
    