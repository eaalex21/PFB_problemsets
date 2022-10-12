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
