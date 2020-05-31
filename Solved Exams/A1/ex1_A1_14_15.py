# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-20 04:38:01
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-20 04:53:53

# ----------- EX. 1 --------------
def quente_ou_frio(number, guess, ex_guess):
	dist1 = abs(number - guess)
	dist2 = abs(number - ex_guess)

	if dist1 < dist2:
		return "Quente"
	else:
		return "Frio"


number_to_guess = int(input("Give a number: ")) #User must write a number to be guessed

for i in range(0,100): #Clear screen with 100 empty lines
	print("")

guess = number_to_guess + 1 #We need to initialize variable and this way we have sure that its not the same as number to guess
score = 0 #Variable to store the score

while (number_to_guess != guess):
	ex_guess = guess #We must store last guess to compare with new one

	guess = int(input("Give a try: ")) #Take a try from user

	if score != 0: #We dont want to call function on first time
		print("{}".format(quente_ou_frio(number_to_guess, guess, ex_guess)))

	score += 1 #Score increment
	

print("You win.\nYour score: {}".format(score))
