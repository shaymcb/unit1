#Shaylee McBride
#24Jan2018
#precalcFunTimes2.py - ah fuck it's compounding interest

from math import log10

startMoney = float(input('Enter starting amount of money: '))
interestRate = float(input('Enter interest rate as decimal: '))
n = float(input('Enter how many times per year your interest is compounded: '))
finalMoney = float(input('Enter the final amount of money you want: '))
time = log10(finalMoney/startMoney)/(n*log10(1+interestRate/n))
print('It will take',time,'years')
