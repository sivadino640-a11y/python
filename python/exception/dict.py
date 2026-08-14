std={"name":"siva","id":"100","address":"rjy"}
try:
    key=input("Enter a key")
    print(std[key])
except KeyError:
    print("Error")
