#!/usr/bin/env python3
# EAA 10.16.2022

# import modules

class DNARecord(object): # creating a DNARecord class and naming it 
	# defining attributes 
	def __init__ (self, sequence, seq_name, species_origin):
		self.sequence = sequence # defining how each attribute will appear
		self.seq_name = seq_name 
		self.species_origin = species_origin
	def sequence_len(self):
		seq_length = len(self.sequence)
		return seq_length
	def nt_composition(self):
		a_count = self.sequence.count("A")
		t_count = self.sequence.count("T")
		g_count = self.sequence.count("G")
		c_count = self.sequence.count("C")
		nt_comp = ('A:' + a_count + ' ' + 'T:' + t_count + 'G:' + g_count + 'C:' + c_count) 
		return nt_comp
	def GC_content(self):
		gc_content = (self.sequence.count("G") + self.sequence.count("C")) / len(self.sequence)
		return gc_content
	def fasta_format(self):
		fasta_for = (self.seq_name + ' ' + self.species_origin + '\n' + self.sequence)
		return fasta_for

dna_seq = input("DNA_sequence:")
dna_seq_name = input("Name of sequence:")
dna_species_origin = input("Name of Origin Species:")

dna_object = DNARecord(dna_seq, dna_seq_name, dna_species_origin)
print("DNA sequence:", dna_object.sequence, "Name of Sequence:", dna_object.seq_name, "Origin Species:", dna_object.species_origin)

print(dna_object.fasta_format())
