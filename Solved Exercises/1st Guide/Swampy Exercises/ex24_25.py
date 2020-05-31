# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-06 11:19:07
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-13 20:14:14

#necessary modules here!!!
from swampy.TurtleWorld import *
import tkinter as tk #using python 3

from math import pi
from math import sin

import sys

# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

#----------------------------------------------------------------------
def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def polygon(t, n, length):
	angle = 360.0 / n
	polyline(t, n, length, angle)

def arc(t, r, angle):
	arc_length = 2 * pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)

def petal(t, r, angle):

	for i in range(2):
		arc(t, r, angle)
		lt(t, 180-angle)

def flower(t, n, r, angle):

	for i in range(n):
		petal(t, r, angle)
		lt(t, 360.0/n)


def draw_pie(t, n, r):
    polypie(t, n, r)
    pu(t)
    fd(t, r*2 + 10)
    pd(t)


def polypie(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)


def isosceles(t, r, angle):
    y = r * sin(angle * pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)

#----------------------------------------------------------------------
# Program starts here
from time import sleep

# make a list
items = list(range(0, 7))
i = 0
l = len(items)

world = TurtleWorld() # Create an instance of TurtleWorld -- i.e, a window
bob = Turtle()        # Create an instance of a Turtle
bob.delay = 0


option = input("Can we start drawing? [y, n]: ")

if option == 'y':
	print("\nPrinting exercise 24 and 25...\n")

	# Initial call to print 0% progress
	printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

	for item in items:

		if item==0:
			#Flowers
			bob.x = -125
			bob.y = 80
			flower(bob, 7, 60, 60)
		if item==1:
			bob.x = 0
			bob.y = 80
			flower(bob, 10, 40, 80)
		if item==2:
			bob.x = 125
			bob.y = 80
			flower(bob, 20, 140, 20)

		if item==3:
			#Geometric pies
			size = 40

			bob.x = -140
			bob.y = -40
			draw_pie(bob, 5, size)
		if item==4:
			bob.x = -40
			bob.y = -40
			draw_pie(bob, 6, size)
		if item==5:
			bob.x = 60
			bob.y = -40
			draw_pie(bob, 7, size)
		if item==6:
			bob.x = 150
			bob.y = -40
			draw_pie(bob, 8, size)

		sleep(0.1)
	    # Update Progress Bar
		i += 1
		printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

else:
	wait_for_user()

wait_for_user()
