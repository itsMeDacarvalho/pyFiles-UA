# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-06 00:27:37
# @Last Modified by:   root
# @Last Modified time: 2016-12-06 00:45:22

import math

#Função para calculo de polinomios
def poly(x, a, b, c):
	return math.pow(x*a, 2) + (x*b) + c

#Parametros para calculo do polinomio
a =  float(input("Parametro 'a': "))
b =  float(input("Parametro 'b': "))
c =  float(input("Parametro 'c': "))
ponto =  float(input("Ponto em que deseja calcular o polinomio: "))

print("x({}) : {}x^2 + {}x + {} ==> {}".format(ponto, a, b, c, poly(ponto, a, b, c)))