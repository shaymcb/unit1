#Shaylee McBride
#1March2018
#graphAPoint.py

from ggame import *

xInput = float(input('Enter the x-coordinate: '))
yInput = float(input('Enter the y-coordinate: '))

if abs(xInput) >= abs(yInput):
    scale = abs(xInput/8)
else:
    scale = abs(yInput/8)
print(scale)

xAxisLocation = 45*(6-3*(xInput/abs(xInput)))
yAxisLocation = 45*(6+3*(yInput/abs(yInput)))
pointXLocation = xInput/scale*45 + xAxisLocation
pointYLocation = yAxisLocation - yInput/scale*45 

black = Color(0x000000,1)
white = Color(0xFFFFFF, 1)

blackOutline = LineStyle(2,black)

window = RectangleAsset(540,540,blackOutline,white)
xAxis = LineAsset(0,540,blackOutline)
yAxis = LineAsset(540,0,blackOutline)
xTick = LineAsset(30,0,blackOutline)
yTick = LineAsset(0,30,blackOutline)
point = CircleAsset(5,blackOutline,black)

#axis
Sprite(window)
Sprite(xAxis,(xAxisLocation,0))
Sprite(yAxis,(0,yAxisLocation))
for i in range(12):
    Sprite(xTick,(xAxisLocation-15,45*i))
    Sprite(yTick,(45*i,yAxisLocation-15))

Sprite(point,(pointXLocation,pointYLocation))

App().run()
