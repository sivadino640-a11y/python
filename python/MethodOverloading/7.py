class Bank:
    def deposit(self,nor,deposit=0):
     total=nor+deposit
     print("Total:",total)
b=Bank()
b.deposit(23)
b.deposit(23,3)