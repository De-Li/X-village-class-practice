def f(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i," * ",j," = ", i*j,end =' ')
        print(end = '\n')
m=int(input("what's M*M = "))
f(m)