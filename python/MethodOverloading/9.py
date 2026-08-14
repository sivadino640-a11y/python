class Shopping:
    def prod(self,TV,AC=0,Fridge=0):
     t=TV+AC+Fridge
     print(t)
p=Shopping()
p.prod(10000)
p.prod(25000)
p.prod(15000)