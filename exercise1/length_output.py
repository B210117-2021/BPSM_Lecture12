#!/usr/local/bin/python3

fr=open('input.txt', 'r')  #read files
fw=open('output.fasta', 'w')  #write files

for line in fr:
    fw.write(line[14:])
    fw.write("\n")
    print(len(line[14:]))
fw.close()



















