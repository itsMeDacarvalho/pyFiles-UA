# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-06 01:28:26
# @Last Modified by:   dacarvalho
# @Last Modified time: 2016-12-06 11:16:40

def sumN(n):
    sum = 0
    for i in range(0,n):
        value = input("Add value: ")
        sum += value

    print("Total sum of entered values: {}".format(sum))

n = input("How many values to sum? ")
sumN(n)
