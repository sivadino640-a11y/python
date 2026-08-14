try:
    num=int(input("enter number:"))
    if num<0:
        raise ValueError("number must be greater than 0")
    else:
        print("The number is:",num)
   
except ValueError:
    print("error:")
    raise
