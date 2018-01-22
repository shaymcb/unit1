#Shaylee McBride
#22Jan2018
#change.py - how many of each coin you need to meet cents

cents = int(input("Input a number in cents: "))
quarters = int(cents/25)
dimes = int((cents - quarters * 25)/10)
nickles = int((cents - quarters * 25 - dimes * 10)/5)
pennies = int(cents - quarters * 25 - dimes * 10 - nickles * 5)
print('Quarters: ', quarters)
print("Dimes: ",dimes)
print("Nickles: ",nickles)
print('Pennies: ',pennies)