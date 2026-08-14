try:
 print("karthik")
 x=int(input("Enter a value"))
 y=int(input("Enter a value"))
 z=x/y
 print(z)
 print("end")
 l1=[1,2.3,"abc"]
 ind=int(input("enter a index value"))
 print(l1[ind])
except (ZeroDivisionError,ValueError,IndexError) as e:
    print("error",e)
finally:
    print("Always executed")
