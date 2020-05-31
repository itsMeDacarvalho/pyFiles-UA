# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-05 20:57:08
# @Last Modified by:   root
# @Last Modified time: 2016-12-05 21:11:17

def countDigits(phrase):
    numOfDigits = 0

    for letter in phrase:
        if letter.isdigit():
            numOfDigits += 1

    return numOfDigits

strToCount = input("Insert string to count how many digits: ")
print("{} have {} digits.".format(strToCount, countDigits(strToCount)))
        
