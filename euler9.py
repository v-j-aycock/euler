import math
x = 2
y = 2
z = 0
while True:
    z = math.sqrt((x**2)+(y**2))
    if z+x+y == 1000:
        break
    elif x < 1000:
        x+=1
    else:
        x=2
        y+=1
print('x=',x,'y=',y,'z=',z)
print(x**2,'*',y**2,'=',z**2)
print(x*y*z)