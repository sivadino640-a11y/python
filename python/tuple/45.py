t=(1,2,3,4,5,6,7)
even=0
odd=0
for i in t:
    if i%2==0:
      print("even:" , i)
      even+=1
    else:
      print("odd:" , i)
      odd+=1
      print("total even numbers:",even)
      print("total odd numbers:",odd)


       