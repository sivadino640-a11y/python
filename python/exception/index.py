try:
    l1=[1,2,4,5,6,7]
    ind=int(input("Enter index"))
    print(l1[ind])
except IndexError:
    print("error")