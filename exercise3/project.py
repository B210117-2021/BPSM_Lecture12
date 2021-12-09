#!/usr/local/bin/python3

import shutil
AJ223353_seq = open('remote_exon.fasta').read().split()[1]  #文件打开

windowsize = 30
offset = 3
segment_starts = list(range(0,len(AJ223353_seq)-windowsize+1,offset))  #设置窗口起始位置

basic_fasta_header = '_window' + str(windowsize) + '_offset' + str(offset) #加header

alloutfilename = 'AJ223353_exon' + basic_fasta_header + '.fasta'
with open(alloutfilename, 'w') as allsegments :
 allsegments.write('')
# Create a blank list to hold the segments
 segments_made = []
# Create a possible yes/no switching variable, i.e. a conditional
 fileswanted = 1
# The for loop
 for seg_bits in segment_starts :
     tempseq = AJ223353_seq[seg_bits :seg_bits+windowsize].upper()
     segments_made = segments_made + [tempseq]
# percentage GC content, convert float to integer value
     tempGC = int(100 * (tempseq.count('G') + tempseq.count('C'))/len(tempseq) )
# make a fasta header line
     descriptionline = 'AJ223353_coding_'+str(len(segments_made))+'_'+tempseq+basic_fasta_header
     fastaheader = '>'+descriptionline
     print(len(segments_made),'\t',tempseq,'\t',tempGC)
# Question : do we want files written? Answer will be either True or False ('maybe' is NOT an option!)
     if fileswanted == 1 :
# open the segment fastafiles
        with open(descriptionline+'.fasta', 'w') as segmentfile :
# output to files
          segmentfile.write(fastaheader+'\n'+tempseq)
          allsegments.write(fastaheader+'\n'+tempseq+'\n\n')
     else :
        allsegments.close()






