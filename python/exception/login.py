us="abc"
ps="1234"
try:
    username=input("enter a username:")
    password=input("enter a password:")
    if username!=us:
     raise ValueError("invalid username")
    if password!=ps:
     raise ValueError("invalid password")
   
except ValueError:
    print("error")
else:
    print("login success")
