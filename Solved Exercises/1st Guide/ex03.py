# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2016-12-05 19:51:12
# @Last Modified by:   root
# @Last Modified time: 2016-12-05 20:40:23

#Calcular média de entrada na UA
Portugues = float(input("Lingua Portuguesa: "))
Ingles = float(input("Ingles: "))
Matematica = float(input("Matematica: "))
FiscaQuimica = float(input("Fisica-Quimica: "))
BiolGeom = float(input("Biologia ou Geometria: "))
Filosofia = float(input("Filosofia: "))
AplInfor = float(input("Aplicacoes Informaticas: "))

ExamePort = float(input("Exame Nacional Portugues: "))
ExameMat = float(input("Exame Nacional Matematica: "))

mediaSecundario = float((Portugues+Ingles+Matematica+FiscaQuimica+BiolGeom+Filosofia+AplInfor)/6
)
notaEntrada = float(mediaSecundario*0.5 + ExameMat*0.5)

print("Nota de entrada na UA: {}".format(notaEntrada))