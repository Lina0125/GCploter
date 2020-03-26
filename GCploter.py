#!/usr/bin/python3
#This program is aim to plot GC content over a genome
#usage:plot_GC_content.py genome.fna 10000 10000 GC_content.jpg

import argparse
import sys
import matplotlib.pyplot as plt

########## Parsing arguments ###########
desc='''This program plot GC content over a fasta sequence.'''
parser=argparse.ArgumentParser(description=desc)
parser.add_argument('i',metavar='input_fasta_file',type=argparse.FileType('r'))
parser.add_argument('w',metavar='window_size',type=int)
parser.add_argument('s',metavar='step',type=int)
parser.add_argument('-o',metavar='output_file',type=argparse.FileType('wb'))
args=parser.parse_args()
########################################

window_size = args.w
step = args.s

#extract whole genome sequence
sequence = ''
with args.i as input:
    for line in input:
        if line.startswith('>'):pass
        else:
            line = line.strip().upper()
            sequence += line

#caculate GC content over whole sequence
y=[]
x=[]
window_start=0
window_end=window_size

while sequence:
    if window_end >= len(sequence):
        break
    else:
        GC_content=int((sequence[window_start:window_end].count('G')+sequence[window_start:window_end].count('C'))\
               *100/window_size)
        y.append(GC_content)
        x.append(window_start+1)
        window_start += step
        window_end += step

#plot GC content over whole sequence
plt.figure(figsize=(20,6))
plt.plot(x,y,'b--',linewidth=1)
plt.xlabel('Position')
plt.ylabel('GC_content(%)')
plt.title('Plot GC content over a genome')
plt.show()

filename=str(sys.argv[1])+'.png'
if args.o:
	plt.savefig(args.o)
else:
    with open(filename,'wb') as output:
        plt.savefig(output)

