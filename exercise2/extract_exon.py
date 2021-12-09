#!/usr/local/bin/python3

fr_dna = open("genomic_dna2.txt")
fr_num = open("exons.txt")
fw = open("extract_exon.txt",'w')


dna_seq = fr_dna.read()
#print(count)

for line in fr_num:
    a = list(line.rstrip().split(","))
    num_1 = int(a[0])-1
    num_2 = int(a[1])-1
    fw.write("This exon is from "+ str(num_1)+" to " + str(num_2))
    fw.write("\n")
    fw.write(dna_seq[num_1:num_2])
    fw.write('\n')
fw.close()





