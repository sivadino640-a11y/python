try:
 file=open("data.txt","r")
 data=file.read()
 print(data)
except FileNotFoundError:
    print("error")