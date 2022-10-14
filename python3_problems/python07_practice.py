#!/usr/bin/env python3
# EAA 10.13.2022

#import packages
import re

# nobody
with open("Python_07_nobody.txt", "r") as py7no_read:
	for line in py7no_read:
		line = line.rstrip()
		for nobody in  re.finditer(r'Nobody', line):
			n1 = nobody.group(0)
			position = nobody.start(0) + 1
			print(n1, position)

# nobody switch with hendrix
with open("Python_07_nobody.txt", "r") as py7no_read, open("Python_07_somebody.txt", "w") as py07hen:
	for line in py7no_read:
		line = line.rstrip()
		somebody = re.sub(r'Nobody','Hendrix', line)
		py07hen.write(f"{somebody}\n")
		print(somebody)
			


# fasta finding header 
with open("Python_07.fasta", 'r') as fasta7:
	for line in fasta7:
		line = line.rstrip()
		for header in re.finditer(r'^>gi.+', line):
			seqID = header.group(0)
			seqID_list = seqID.split()
			desc = ' '.join(seqID_list[1:])
			print('id:' + str(seqID_list[0]) + ' ' + 'desc:' + desc)
