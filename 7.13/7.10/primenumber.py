i=1
x=int(input("enter a range: "))
while i<x:
    temp=0
    if i%2!=0:
        if i%3!=0:
            if i%5!=0:
                if i%7!=0:
                 print("prime number = ",i)
    i+=1
