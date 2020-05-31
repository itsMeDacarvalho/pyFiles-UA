# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-24 02:45:01
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-24 02:59:43

def giveName(names, numbers, numberToSearch):
	i = 0
	flag = False

	for number in numbers:
		if number == numberToSearch:
			flag = True
			break
		else:
			i += 1

	if flag == False:
		return "Name not found."
	else:
		return names[i]


names = ["Daniel", "Tatiana", "Patrick"]
numbers = [969832912, 926568221, 962334678]

numberToSearch = int(input("Number to search: "))

print("The number {} belongs to {}".format(numberToSearch, giveName(names, numbers, numberToSearch)))
