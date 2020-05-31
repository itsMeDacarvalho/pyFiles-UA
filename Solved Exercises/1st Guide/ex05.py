# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-05 20:57:08
# @Last Modified by:   root
# @Last Modified time: 2016-12-05 21:11:17

#1 morador por piso
#3 pisos (com R/C incluido) -> R/C nao necessita de elevador
#3m - altura de cada piso

distanceToPick1 = 3*2*365 #percorre 3m 2 vezes por dia durante 365 dias
distanceToPick2 = 6*2*365 #percorre 6m 2 vezes por dia durante 365 dias
distanceToPick3 = 9*2*365 #percorre 9m 2 vezes por dia durante 365 dias

totalDistanceInMeters = distanceToPick1+distanceToPick2+distanceToPick3

totalDistanceToKm = totalDistanceInMeters * 0.001

print("Distancia percorrida pelo elevador por ano: {0:.3f} km".format(totalDistanceToKm))