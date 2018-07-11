import math
def sqrt(a,b,c):
    ans=math.sqrt(b**2-4*a*c)
    return ans 

a=int(input("input a:"))
b=int(input("input b:"))
c=int(input("input c:"))
ans1=(-b+sqrt(a,b,c))/2*a
ans2=(-b-sqrt(a,b,c))/2*a
print(ans1,",",ans2)


