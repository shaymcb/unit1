#Shaylee McBride
#22Jan2018
#isItATriangle.py - is it a triangle?

sideA = float(input("Enter Side A: "))
sideB = float(input("Enter Side B: "))
sideC = float(input("Enter Side C: "))
bigside = max(sideA,sideB,sideC)
smallside = min(sideA,sideB,sideC)
midside = sideA + sideB + sideC - bigside - smallside
print(midside + smallside < bigside)