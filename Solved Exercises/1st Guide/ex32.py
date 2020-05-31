# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-11 05:16:51
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-11 05:31:15

def shrinkPhrase(phrase):
	
	if len(phrase) <= 140:
		return "[ERROR] Only shrink strings with more than 140 characters!"

	else:
		tmp = ""
		counter = 0
		for character in phrase:
			if counter==140:
				"Shrinking to 140 characters..."
				return tmp
			else:
				tmp += character

			counter += 1

textToShrink = input("Please insert the text you want to shrink (>140 chars): \n")
print("\nShrinked text:\n{}".format(shrinkPhrase(textToShrink)))