# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-20 04:55:46
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-20 05:41:10

# ----------- EX. 2 --------------
def encode(phrase, key):
	phrase = phrase.split() #Create list with single words in each position

	original = 'abcdefghijklmnopqrstuvwxyz'
	encoded = "" #String to store the encoded string to return later

	for word in phrase:

		for letter in word: #Go letter by letter in list created from string
			i = 0 #Variable to store index of letter in alphabet

			for alphabet_char in original: #Go char by char in alphabet list
				if letter.lower() == alphabet_char.lower(): #All char to lower case, this way we have sure that everything go well!
					break

				i += 1 #Update index

			encoded = encoded + key[i] #Go in received key and pick the right letter to append on the string that we will return
		
		encoded = encoded + " " #Print space between words
	return encoded

def decode(phrase, key):
	phrase = phrase.split() #Create list with single words in each position

	original = 'abcdefghijklmnopqrstuvwxyz'
	decoded = "" #String to store the encoded string to return later

	for word in phrase:

		for letter in word: #Go letter by letter in list created from string
			i = 0 #Variable to store index of letter in alphabet

			for alphabet_char in key: #Go char by char in alphabet list
				if letter.lower() == alphabet_char.lower(): #All char to lower case, this way we have sure that everything go well!
					break

				i += 1 #Update index

			decoded = decoded + original[i] #Go in received key and pick the right letter to append on the string that we will return
		
		decoded = decoded + " " #Print space between words
	return decoded


option = -1

while option != 0:
	phrase = input("Give some phrase: ")
	key = "defghijklmnopqrstuvwxyzabc"

	option = int(input("ENCODE   [1]\nDECODE   [2]\nEXIT     [0]\n>> "))

	if option == 0:
		break

	elif option == 1:
		print("\nOriginal: {}\nEncoded: {}\n".format(phrase, encode(phrase, key)))

	elif option == 2:
		print("\nOriginal: {}\nDecoded: {}\n".format(phrase, decode(phrase, key)))
	else:
		print("Invalid option!")

	

	
