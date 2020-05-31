# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-11 05:32:17
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-11 05:41:52

def getAbbreviation(name):
	
	splitted = name.split()

	abbreviation = ""
	tmp = ""
	for word in splitted:
		if len(word)>2:
			tmp = word[0].upper()
			abbreviation = abbreviation + tmp + "."

	return abbreviation

name = input("Get abbreviaton for: ")
print(getAbbreviation(name))