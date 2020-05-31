# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-29 02:31:49
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-29 03:27:52

def numberToName(number, contacts):
	for key in contacts:
		if contacts[key] == number:
			break

	return key


contacts = {
			'Daniel': 969832912,
			'Patrick': 926568221,
			'Tatiana': 962334678
			}

print("Name: {} \nNumber: {}".format(numberToName(962334678, contacts), 962334678))