x=0
def hanoi(n, a, b, c):
    global x
    if n == 1:
        x+=1
		#print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1    , a, b, c)
        hanoi(n - 1, b, a, c)
# 调用
hanoi(64, 'A', 'B', 'C')
print(x)
