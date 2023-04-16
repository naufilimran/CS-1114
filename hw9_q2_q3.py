
####Author: Naufil Bin Imran
##Assignment / Part: HW9 - Q2-Q3
##Date due: 2022-04-28
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.



import os

def create_entry(number,name,type_1,type_2,health_points,attack,defense,special_attack,special_defense,speed,generation,is_legendary):
    types=(type_1,type_2)
    if type_2=="":
      types=(type_1,None)
    battle_stats="Battle Stats"
    battle_stats_dictionary={"HP":health_points,"Attack": attack, "Defense":defense,"Sp.Atk":special_attack,"Sp.Def":special_defense,"Speed": speed}
    dictionary={"Number":number,"Name":name,"Types":types,"Battle Stats": battle_stats_dictionary,"Generation":generation,"Legendary":is_legendary}
    
    return dictionary    

def create_pokedex(filepath):
    if os.path.exists(filepath):
        pokedex = {}
        file = open(filepath, 'r')
        content = file.readlines()
        header = content[:1][0].strip()
        for line in content[1:]:
            rows = line.strip() 
        file.close()
        for row in rows:
            row = row.split(',')
            pokedex[row[1]] = create_entry(row[1], row[2], row[3], row[4],row[5],row[6], row[7], row[8], row[9], row[10], row[11], row[12])

        return pokedex
    else:
        return {}


def main():
    filepath = "pokemon.csv"
    pokedex = create_pokedex(filepath)
    pokemon_key = "Venusaur"

    try:
        my_favorite_pokemon = pokedex[pokemon_key]
    except KeyError:
        print("ERROR: Pokemon {} does not exist!".format(pokemon_key))
    else:
        print("PRINTING {}'S INFORMATION...".format(pokemon_key))
        for key in my_favorite_pokemon.keys():
            print("{}: {}".format(key, my_favorite_pokemon[key]))


if __name__ == '__main__':
    main()
