#Shaylee McBride
#25Jan2018
#precalcFunTimes4.py - exponentially worse

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
x3 = float(input('Enter x3: '))
b = (y2/y1)**(1/(x2-x1))
a = y1/(b**x1)
y3 = a*b**x3
print('f(',x3,') =',y3)
