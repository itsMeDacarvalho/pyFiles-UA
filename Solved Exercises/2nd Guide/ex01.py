# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-24 01:56:31
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-24 02:43:28

def length(lst):
	i = 0

	for item in lst:
		i = i +1

	return i


def readList():
	tmplist = []

	while True:
		tmp = input("Append something to list: ")
		tmplist.append(tmp)

		if tmp == "":
			break

	return tmplist


def sumList(lst):
	sum = 0

	for item in lst:
		sum = sum + float(item)

	return sum


def lessThan(lst, number):
	counter = 0

	for item in lst:
		if item < number:
			counter += 1

	return counter

def maxInList(lst):
	
	if length(lst) > 0:
		max = lst[0]

		for item in lst:
			
			if item >= max:
				max = item

		return max

	else:
		return 0

def maxHalf(lst):

	if length(lst) > 0:
		print("Maximum value in list is: {}".format(maxInList(lst)))

		halfMax = maxInList(lst)/2

		print("{} values are less than half of maximum value.".format(lessThan(lst, halfMax)))

	else:
		print("List is empty!!!")

def changeValues(lst, x, y):
	i = 0

	if length(lst) > 0:
		
		for item in lst:
			if item == x:
				lst[i] = y
			i += 1

		return lst

	else:
		return lst


def invertList(lst):
	
	if length(lst) > 0:
		revList = []

		for i in range(length(lst)-1, -1, -1):
			revList.append(lst[i])

		return revList

	else:
		return lst

lst = [2,4,6,8]

print("Size: {}".format(length(lst)))

newList = readList()
print(newList)

print("Sum of the values in list: {}".format(sum(lst)))

print("Number of values in list less than {} is {}.".format(6, lessThan(lst, 6)))

maxHalf(lst)

changedList = changeValues(lst, 2, 8)
print(changedList)

invList = invertList(lst)
print(invList)








