#Shaylee McBride
#25Jan2018
#precalcFunTimes3.py - more intense triangling

from math import acos, degrees, asin, sin

sideA = float(input('Enter side A: '))
sideB = float(input('Enter side B: '))
sideC = float(input('Enter side C: '))
angleA = acos((sideB**2+sideC**2-sideA**2)/(2*sideB*sideC))
angleB = asin((sideB*sin(angleA))/(sideA))
angleC = asin((sideC*sin(angleA))/(sideA))
print('Angle A is',degrees(angleA),'degrees')
print('Angle B is',degrees(angleB),'degrees')
print('Angle C is',degrees(angleC),'degrees')
print('The area of the triangle is',(sideA*sideB*sin(angleC))/2)