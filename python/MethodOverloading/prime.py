numbers=(1,2,3,4,5)
for num in numbers:
    if num>1:
    is_prime=true
    for i in range(2,n+1):
      if num%i==0:
        is_prime=false
        break
      if is_prime:
        print(i)