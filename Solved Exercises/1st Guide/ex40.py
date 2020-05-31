# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-13 16:47:54
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-13 18:03:31

import os

def solveWords(wordToSearch, whereToSearch): #solve puzzle given word and an dict where can search
	filledPositions = getFilledPositions(wordToSearch)

	tmpList = []

	for word in whereToSearch:
		checkFlag = False

		if len(word) == len(wordToSearch): #verify if dict word have same length as desired word

			for i in filledPositions:
				if word[i] == wordToSearch[i]:
					checkFlag = True
				else:
					checkFlag = False
					break

		if checkFlag == True:
			tmpList.append(word)
	
	return tmpList


def getFilledPositions(wordToSearch): #get positions with desired letter

	filledPositions = []

	for i in range(0,len(wordToSearch)):
		if wordToSearch[i] != '-':
			filledPositions.append(i)

	return filledPositions


def printList(listToPrint): #print a list given
	for word in listToPrint:
		print("-> {}".format(word))


# ------- MAIN -------

print("HOW TO USE: Write the desired word to find but put '-' on blank spaces!\n")
os.chdir("/usr/share/dict/")

file = open("words", 'r')

wordsList = []

while True: #read dictionary to a list
	tmp = file.readline()
	
	if ("" == tmp):
		break
	
	else:
		wordsList.append(tmp.rstrip()) #rstrip() removes '\n' in the end of string

print("Getting words from dict...\n")

wordToSearch = input("Write the desired word to search: ")
print("-------------------------------\nThis words can be what you want\n-------------------------------")
printList(solveWords(wordToSearch, wordsList)) #find words like desired word input

