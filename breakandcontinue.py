x=0
while x<10:
    print('x is currently: ',x)
    print('x is still less then 10, ading 1 to x')
    x+=1
    if(x==3):
        print('breaking because x==3')
        break
    else:
        print('continuing')
        continue