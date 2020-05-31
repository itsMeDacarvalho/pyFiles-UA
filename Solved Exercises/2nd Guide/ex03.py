# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-24 02:45:01
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-01-25 02:59:43

upper = int(input("Enter upper range: "))

print("Prime numbers between 1 and",upper,"are:")

primes = []

for num in range(1,upper + 1):
    if num > 1:
        for i in range(2,num):
           if (num % i) == 0:
               break
        else:
            primes.append(num)

print(primes)



