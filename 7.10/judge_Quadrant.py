def judge(x,y):
 if x>0:
    if y>0:
      print('first quadrant')
    elif y<0:
      print('fourth quadrant')
    else:
      print('on the axis')      
 else:
      if y>0:
         print('second quadrant')
      elif y<0:
         print("third quadrant")
      else:
         print('on the axis')
x=int(input("X coordinate:"))
y=int(input("Y coordinate:"))
judge(x,y)
