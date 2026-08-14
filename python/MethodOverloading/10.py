class Temperature:
    def convert(self,c):
        k=c+273
        print("celsius to kelvin:",k)
        f=(c*9/5)+32
        print("celsius to fahrenhiet:",f)
t=Temperature()
t.convert(2)
