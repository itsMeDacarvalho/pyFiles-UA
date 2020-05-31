# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-13 18:03:38
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-13 19:20:10

#Please use values.txt to test this file
fileName = input("Please give the file name: ")

file = open(fileName, 'r')

sum = 0

while True:
	tmp = file.readline()

	if tmp == "":
		break

	else:
		sum += float(tmp)

print("The sum of the values in {} file is: {:.3f}".format(fileName, sum))