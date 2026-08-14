class Employee:
    def salary(self,basic,bonus=0):
     total=basic+bonus
     print("Total salary:",total)
e=Employee()
e.salary(20000)
e.salary(20000,500)
