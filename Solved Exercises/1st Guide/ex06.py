# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-05 21:06:01
# @Last Modified by:   root
# @Last Modified time: 2016-12-05 23:57:54

#1 morador por piso
#3 pisos (com R/C incluido) -> R/C nao necessita de elevador
#3m - altura de cada piso
#1 m/s - velocidade do elevador

distanceToPick1 = 3*2*365 #percorre 3m 2 vezes por dia durante 365 dias
distanceToPick2 = 6*2*365 #percorre 6m 2 vezes por dia durante 365 dias
distanceToPick3 = 9*2*365 #percorre 9m 2 vezes por dia durante 365 dias

totalDistanceInMeters = distanceToPick1+distanceToPick2+distanceToPick3

totalDistanceToKm = totalDistanceInMeters * 0.001

print("Tempo em funcionamento durante um ano(horas): {0:.3f} horas".format(totalDistanceInMeters/3600))
