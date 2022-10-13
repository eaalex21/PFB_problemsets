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

# using input f(x)
favs_thing = 'book\tsong\ttree\torganism'
favs_st = input("What is your favorite: " + favs_thing)
print("Here are your options: ", favs_st)

favs_thing = 'song'
favs_st = input("What is your favorite " + favs_thing)
print("This is your favorite song:",favs_st)

#use for loop to call from dict
for things in favs:
	print(things, favs[things])
