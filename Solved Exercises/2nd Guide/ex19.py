# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-24 04:12:55
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-01-24 04:00:05

filename = input("Name of original file: ")
word_to_change = input("Desired word to remove: ")
sub_word = input("Substitution word: ")

fout_filename = "new_" + filename

print("Writing to {}".format(fout_filename))

fin = open(filename, 'r')
fout = open(fout_filename, 'w+')

while True:
    line = fin.readline()
    if line == "":
        break
        
    line = line.split()
    
    new_line = ""
    
    for word in line:
        if word == word_to_change:
            new_line = new_line + " " + sub_word
        else:
            new_line = new_line + " " + word

    fout.write(new_line)
    fout.write("\n")

fout.close()
