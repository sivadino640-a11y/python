class Payment:
    def pay(self):
        print("payment")
class Credit(Payment):
    def pay(self):
        print("credit")
class UPI(Payment):
    def pay(self):
        print("upi")
class Cash(Payment):
    def pay(self):
        print("cash")
c=Credit()
u=UPI()
c1=Cash()
c.pay()
u.pay()
c1.pay()
