#Shaylee McBride
#19Jan2018
#stringAnalysis.py - reports words and characters in a string

sentence = input('Enter a sentence: ')
words = sentence.count(" ") + 1
print("Your sentence has",words, "words,",len(sentence),"characters and",len(sentence) - sentence.count(" "),"letters.")
letter = input("Enter a character to search for: ")
print("Your sentence has",sentence.count(letter),"occurences of the character",letter)
