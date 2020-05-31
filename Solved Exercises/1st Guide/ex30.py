# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-05 20:57:08
# @Last Modified by:   root
# @Last Modified time: 2016-12-05 21:11:17

#Capitalizar primeira letra de cada palavra numa frase

def capsFirst(phrase):
    splited = phrase.split()
    capitalizedPhrase = ""

    for word in splited:
        tmp = word.capitalize()
        capitalizedPhrase += " " + tmp

    return capitalizedPhrase

toCapStr = input("Insert the string you want to capitalize: ")
print("{} -> {}".format(toCapStr, capsFirst(toCapStr)))
