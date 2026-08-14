class Bank:
    def withdraw(self,a,withdrawal):
        print("Balance",a)
        t=a-withdrawal
        print("After withdraw:",t)
       
class Saving(Bank):
    def withdraw(self,b,t=0):
        print("Saving:",b)
        t1=b+t
        print("After saving:",t1)
       
b=Bank()
s=Saving()
b.withdraw(3000,300)
s.withdraw(200,2700)
