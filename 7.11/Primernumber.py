i=1
prime = [2,3,5,7]
x=int(input("enter a range: "))
while i<x:
    temp=0
    j=0
    for j in range(len(prime)):
     if i%prime[j]==0:
         temp+=1
    if temp<=1:
        print("prime number = ",i)
        prime.append(i)
    i+=1
