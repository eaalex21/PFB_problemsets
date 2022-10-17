#!/usr/bin/env python3
# EAA 10.12.2022

# string to list using split f(x)
taxa = 'sapiens, erectus, neanderthalensis'
taxa
print(taxa[1])
type(taxa) # checking variable type of taxa
species = taxa.split(',') # spliting string into list
species
species[1]
type(species) # check type of species
sorted(species, key = str.lower)
sorted(species, key = len)

# using of while loops
hundred = 1
while hundred <= 100:
	print(hundred)
	hundred += 1
print('Done')

fac = 1
i = 1 
while i <= 1000:
	fac =  fac * 1
	i = i + 1
num = 1000
count = 1
factorial = 1

while count <=1000:
	factorial + factorial*count
	count = count+1
print(factorial)

# iterate through list
list1 = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
list1_it = iter(list1)
for num in list1_it:
  if num%2 == 0:
    print(num)
sume = 0
sumo = 0
list1sorted = sorted(list1)
list1sorted_it = iter(list1)
for num in list1sorted_it:
	if num%2 == 0:
		sume += num
	else:
		sumo += num
	print(num)
print(sume)
print(sumo)

# range 0-99
for number in range(100):
	print(number)

# counting to 100 with list comprehension
hundred = [number + 1 for number in range(100)]
print(hundred)

# list for data 
dna = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in dna:
	length = len(seq)
	print(length + '\t' + seq)

# list tuples
lengths = [str(len(dna)) + '\t' + seq + '\n' for dna in dna]
print(lengths)

# modified list 
position = [str(dna.index(seq) + 1) + '\t' + str(len(seq)) + '\t' + seq + '\n' for seq in dna]
print(position)


 
