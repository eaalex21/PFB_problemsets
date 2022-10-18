#!/usr/bin/env python3

import sys
import re

sequence = sys.argv[1]
n_kmers = len(sequence) - int(sys.argv[2]) + 1
kmers_list = []
for i in range(n_kmers):
	kmer = sequence[i:i + int(sys.argv[2])]
	kmers_list.append(kmer)
print(kmers_list)

#list to str
kmer_new = ''.join(kmers_list)
print(kmer_new)
# count kmers and make a dict
kmer_count_dict = {}
for kmer in kmers_list:
	if kmer in kmer_count_dict:
		kmer_count_dict[kmer] += 1
	else:
		kmer_count_dict[kmer] = 1
print(kmer_count_dict)	
