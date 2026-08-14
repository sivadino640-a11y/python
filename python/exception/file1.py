try:
    file=open("data.txt","r")
    content=file.read()
    print(content)
    cls1=file.close()
    print(cls1)
except FileNotFoundError:
    print("error")
