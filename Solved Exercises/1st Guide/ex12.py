# -*- coding: utf-8 -*-
# @Author: dacarvalho@ua.pt
# @Date:   2016-12-05 21:23:25
# @Last Modified by:   root
# @Last Modified time: 2016-12-06 00:18:07

#Ler linhas de um ficheiro de texto e alinhar cada linha a direita


file = open("text.txt", "r")
newFile = open("textAligned.txt", "w")

shifter = ""
tmp=" "

while tmp != "":
	tmp = file.readline()
	newFile.write("{:69}{}".format(shifter, tmp))

file.close()
newFile.close()

print("File text.txt aligned to the right ==> textAligned.txt")