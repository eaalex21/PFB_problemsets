#!/usr/bin/env python3
#EAA 10.14.2022

#import modules
import re

# calc nt comp within a data structure
dna = {}
nt_count = {}
with open("Python_08.fasta", 'r') as py08, open('Python_08truncated.fasta', 'w') as py08_write:
	for line in py08:
		if line.count <= 25:
			py08_write.write(line)

with open('Python_08truncated.fasta', 'r') as py08_read:
	for line in py08_read:
		print(line)
	
