# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-13 18:13:27
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-13 19:20:12

#Use orders.tsv in repository to test this file
def createListFromFile(fileToRead):
	tmpList = []

	splitted = []

	while True:
		tmp = fileToRead.readline()

		if tmp == "":
			break

		splitted = tmp.split('\t') #create a list with values in string spaced by tab char

		tmpList.append(splitted[0])
		tmpList.append(float(splitted[1].rstrip())) #remove newline char in the end of the line

	return tmpList

def sumByCategory(listToRead, category):
	sum = 0

	for i in range(0, len(listToRead)):
		if listToRead[i] == category:
			sum += listToRead[i+1]

	return sum

fileName = input("Give the name of the file with info: ")

file = open(fileName, 'r')

category= input("Category to sum: ")

print("Total spent in {} products: {}".format(category, sumByCategory(createListFromFile(file), category)))