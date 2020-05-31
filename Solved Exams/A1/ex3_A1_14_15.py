# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-20 05:46:19
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-20 06:16:38

# ----------- EX. 3 --------------
def kmPerDay(steps):
	km = (steps * 1.2)* 0.001

	return km

def caloriesPerDay(km):
	calories = km * 32

	return calories

def kmPerWeek(steps):
	week_km = (steps * 1.2) * 0.001

	return week_km

def averageCalories(km):
	average = (km * 32) / 7

	return average

file = open('steps.txt', 'r') #Open steps.txt file and give 'read' permission

daySteps = 0
weekSteps = 0

for i in range(0,7):
	daySteps = int(file.readline()) #Convert to integer the file line with number of steps

	print("Day [{}]".format(i+1))
	print("Km: {:.2f}".format(kmPerDay(daySteps)))
	print("Calories: {:.2f}".format(caloriesPerDay(kmPerDay(daySteps))))
	print("")

	weekSteps += daySteps

print("\n--- This week ---")
print("Total Km: {:.2f}".format(kmPerWeek(weekSteps)))
print("Average calories: {:.2f}".format(averageCalories(kmPerWeek(weekSteps))))
