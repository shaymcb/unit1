#Shaylee McBride
#22Jan2018
#additionGameDemo.py - how to use random numbers

from random import randint

num1 = randint(-10,10)  #pseudorandom, not truly random
num2 = randint(-10,10)
answer = int(input(str(num1)+" + "+str(num2)+' = '))  #connect strings w +, call var strings
print(answer == num1 + num2)
