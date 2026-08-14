animal=["cat,","lion","dog"]
try:
    ind=int(input("Enter a index"))
    print("Animal name is:",animal[ind])
except IndexError:
    print("error")