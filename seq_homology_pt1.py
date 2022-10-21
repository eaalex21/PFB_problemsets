#!/usr/bin/env python3
#Elaine Aquino

#import modules
import sys 
import re

#data 
blast_results = open(sys.argv[1:], 'r') # [1:] allows you to run though each individual file in one line
blast_dict = {}
blast_file = [] #added from answer
blast_list = [] #added from answer
field_names = ('qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits')
for line in blast_results:
	line = line.rstrip()
	if line.startswith('#') == False: 
		blast_dict = dict(zip(field_names, line.split('\t')))
		blast_dict['file'] = blast_file #added from answer
		blasts_list.append(blast_dict) #added from answer
		break #you only top hit or first line that fits criteria

for hit in blasts_list: #added from answer
			
print(blast_dict)	
