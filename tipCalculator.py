#Shaylee McBride
#17Jan2018
#tipCalculator.py - calculates how much you should tip

priceMeal = float(input('Price of meal ($): '))
tipPercent = float(input('Percent to tip: '))
print('You should tip',round(priceMeal*tipPercent*0.01,2),'dollars')
