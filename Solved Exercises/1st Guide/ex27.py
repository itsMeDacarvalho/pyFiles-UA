# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-06 01:28:26
# @Last Modified by:   dacarvalho
# @Last Modified time: 2016-12-06 11:16:40

def fibonacci(n):

    if n == 0: return 0
    if n == 1: return 1

    return int(fibonacci(n-1)) + int(fibonacci(n-2))

n = int(input("Which fibonacci member you want? \n >> "))
print("Fibonacci member calculated: {}".format(fibonacci(n)))
