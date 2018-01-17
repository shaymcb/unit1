#Shaylee McBride
#17Jan2018
#nameAge.py - tells you stuff based on your name and age

name = input("Enter your first and last name: ")
age = int(input('Enter your age: '))
firstName, lastName = name.split()    #splits a string
print('Your first name has',len(firstName),'letters')  #len counts characters in a string
print('Your last name has',len(lastName),'letters')
print('Next year you will be',age+1,'years old')