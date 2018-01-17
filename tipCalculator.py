#Shaylee McBride
#17Jan2018
#tipCalculator.py - calculates how much you should tip

priceMeal = int(input('Price of meal ($): '))
tipPercent = int(input('Percent to tip: '))
print('You should tip',round(priceMeal*tipPercent*0.01,2),'dollars')
