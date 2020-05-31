# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-11 08:48:41
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-13 17:45:21

def palindrome(phrase):
	
	tmp = ""

	for letter in range(len(phrase)-1, -1, -1):
		tmp += phrase[letter]

	if tmp.lower() == phrase.lower():
		return True
	else:
		return False

phrase = input("Verify if it is palindrome: ")

if palindrome(phrase):
	print("'{}' is palindrome!".format(phrase))
else:
	print("'{}' isn't a palindrome!".format(phrase))