# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-06 00:45:38
# @Last Modified by:   root
# @Last Modified time: 2016-12-06 00:52:15

#Calcular o maximo de tres numeros
def max3(a,b,c):
	max = a

	if b >= max:
		return b
	elif c >= max:
		return c
	else:
		return a

#Parametros de execuçao
a = float(input("Primeiro numero: "))
b = float(input("Segundo numero: "))
c = float(input("Terceiro numero: "))

print("\nO maximo valor em [{}, {}, {}] é {}".format(a, b, c, max3(a,b,c)))