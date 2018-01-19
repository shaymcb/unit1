#Shaylee McBride
#19Jan2018
#slope.py - finds slope given two points

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
slope = (y2 - y1)/(x2 - x1)
print("The slope is",slope)
print('The equation of the line is y =',slope,'x +',y1-slope*x1)
