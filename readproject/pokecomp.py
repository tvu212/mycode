#!/usr/bin/env python3

import csv
import random

#Randomly select 6 pokemon to be a part of a battle composition  
with open("pokedex.txt") as pokedata:
    pokecomp = []                        #declares early list of pokemon
    pokelist = []                        #declares table of pokemon to reference to
    csv_reader = csv.reader(pokedata)
    for row in csv_reader:
        pokelist.append(row)

    print("Here are your randomly assigned pokemon:")
    for i in range(6):
        pokenum = random.randint(1,721)  #randomly select pokenumber
        pokecomp.append(pokelist[pokenum])

    for pokemon in pokecomp:
        print(f"{pokemon[1]} is a {pokemon[2]}/{pokemon[3]} pokemon with a base health stat of {pokemon[5]}" )

        
