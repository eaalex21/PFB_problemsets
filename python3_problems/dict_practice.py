#!/usr/bin/env python3
# EAA 10.13.2022

favs = {'book':'To Kill A Mockingbird', 'song' : 'Sanga Zoo' , 'tree' : 'Cedar'}
print(favs['book'])

favs_thing = 'book'
print(favs[favs_thing])

print(favs['tree'])

favs['organism'] = 'E.coli'
print(favs)

favs_things = 'organism'
print(favs[favs_things])

str = input('key options')
print("Here are your options:", str)

