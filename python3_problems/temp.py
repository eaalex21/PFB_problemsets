# calc nt comp
  9 for py8_record in SeqIO.parse('Python_08.fasta', "fasta"):
 10   for nt in py8_record.seq
 11     
 12

 if seqID not in dna:
 20         dna[seqID] = {}
 21     else:
 22       sequence = line
 23       if sequence not in dna[seqID]:
 24         dna[seqID][sequence]: {}    
 25       print(dna[seqID][sequence])  



 if line.startswith('>'):
 17       line = line.rstrip('\n')
 18       header = line.rsplit()
 19       seqID = header[0]
 20       length = header [1]
 21       path = header[2]
 22       if seqID not in dna:
 23         dna[seqID] = {}
 24     else:
 25       sequence = line.rstrip('\n')
 26       if sequence not in dna:
 27         dna[seqID] = sequence
 28     print(dna)
 29   
 
