std={"name":"karthik","age":"18"}
try:
    print(std["age"])
except KeyError:
    print("Error")
