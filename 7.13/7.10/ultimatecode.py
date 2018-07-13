import random
code=random.randint(0,100)
guess=int(input("guess a number 1~100: "))
uppertemp=100
lowwertemp=0
while guess!=code:
    if guess<uppertemp | guess>lowwertemp:  
     print('wrong guess','try a again')
     if guess > code:
          uppertemp = guess
          print('next range is ', lowwertemp ,'~', uppertemp )
     elif code > guess:
          lowwertemp=guess
          print('next range is ', lowwertemp ,'~', uppertemp )
    else:
         print('out of range , try again')
         print('next range is ', lowwertemp ,'~', uppertemp )
    guess=int(input("guessnext number : "))
print('correct,awesome!!')
