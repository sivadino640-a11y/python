class Online:
    def Payment(self):
        print("online payment")
class Card:
    def Payment(self):
        print("card payment")
class Cash:
    def Payment(self):
        print("cash payment")
def payment1(obj):
    obj.Payment()
o=Online()
c=Card()
c1=Cash()
payment1(o)
payment1(c)
payment1(c1)


