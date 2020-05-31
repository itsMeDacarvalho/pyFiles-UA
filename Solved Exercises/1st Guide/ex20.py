# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-06 01:28:26
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-25 02:55:30

#Determinar o numero de digitos num numero
numero = input("Numero: ")

if int(numero) < 0:
	print("Deve introduzir apenas numeros inteiros positivos.")
else:
	print("O numero '{}'' tem {} digitos.".format(numero, len(numero)))