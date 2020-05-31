# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-24 04:12:55
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-28 04:00:05

def fileToList(file):
	lst = []

	while True:
		tmp = file.readline()
		

		if tmp == "":
			break
		else:
			tmp = tmp.rstrip().split(',')
			for player in tmp:
				lst.append(player)

	return lst

def averageOfDef(teamList):
	numberOfPlayers = len(teamList)/4
	sumOf = 0
	sumDef = 0

	for i in range(0,len(teamList),4):
		sumDef = sumDef + int(teamList[i+2])
		sumOf = sumOf + int(teamList[i+3])

	return (sumDef/numberOfPlayers, sumOf/numberOfPlayers)

team = open("team.txt", 'r')
lst = fileToList(team)
print(averageOfDef(lst))
