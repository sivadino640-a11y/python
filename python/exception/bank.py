balance=3000
try:
    amount=int(input("Enter a amount"))
    if amount<=0:
        raise ValueError("error")
    if amount>balance:
     raise ValueError("insufficient")
    else:
     balance=balance-amount
     print(balance)
except ValueError as error:
    print("error",error)
    