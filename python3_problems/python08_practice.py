#!/usr/bin/env python3
#EAA 10.14.2022

# calc nt comp within a data structure
dna = {}
nt_count = {}
with open("Python_08.fasta", 'r') as py08:
	for line in py08:
		line = line.rstrip()
		seqID, length, seq = line.split()
		dna[seqID] = seq
	print(dna)
