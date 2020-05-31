# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-06 00:19:04
# @Last Modified by:   root
# @Last Modified time: 2016-12-06 00:45:07

#Calculo do IMC
def IMC(peso, altura):
	return peso/altura

#Pedir dados para execução do calculo
peso = float(input("Peso(kg): "))
altura = float(input("Altura(m): "))

print("O seu IMC: {:.2f}".format(IMC(peso, altura)))