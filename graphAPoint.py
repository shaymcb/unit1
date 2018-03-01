#Shaylee McBride
#1March2018
#graphAPoint.py

from ggame import *

xInput = float(input('Enter the x-coordinate: '))
yInput = float(input('Enter the y-coordinate: '))

black = Color(0x000000,1)
white = Color(0xFFFFFF, 1)
xAxisLocation = 45*(6-2*(xInput/abs(xInput)))
yAxisLocation = 45*(6+2*(yInput/abs(yInput)))

blackOutline = LineStyle(2,black)

window = RectangleAsset(540,540,blackOutline,white)
xAxis = LineAsset(0,540,blackOutline)
yAxis = LineAsset(540,0,blackOutline)
xTick = LineAsset(0,30,blackOutline)
yTick = LineAsset(30,0,blackOutline)

Sprite(window)
Sprite(xAxis,(xAxisLocation,0))
Sprite(yAxis,(0,yAxisLocation))
    

for i in range(12):
    Sprite(xTick, (45*i,xAxisLocation-15))
    Sprite(yTick, (yAxisLocation-15,45*i))

App().run()
