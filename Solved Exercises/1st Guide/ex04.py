# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-05 20:43:14
# @Last Modified by:   root
# @Last Modified time: 2016-12-05 21:11:28

#Tempo medio por km
#Velocidade media em km/h
#1mile -> 1,61km

mileToKm = 1.61*10
timeToHours = (43*60 + 30)/3600

print("Tempo médio por km(s): {0:.2f} segundos".format((timeToHours*3600)/mileToKm))
print("Velocidade média(km/h): {0:.2f} km/h".format(mileToKm/timeToHours))

#Os prints foram formatados para apresentar apenas 2 casas decimais