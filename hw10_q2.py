
##Author: Naufil Bin Imran
##Assignment / Part: HW10 - Q2 
##Date due: 2022-04-28
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.




import random
from hw10_q1 import Weapon
class Duelist:
    def __init__(self,duelist_name, weapon_inventory):
        self.duelist_name = duelist_name
        self.weapon_inventory = weapon_inventory
        self.number_of_weapons = len(weapon_inventory)

    def __str__(self):
        string_final = "Duelist Object '{}', carrying ".format(self.duelist_name)

        for object in range(len(self.weapon_inventory)-1):
            string_final += self.weapon_inventory[object].weapon_name+ ", "
        

        string_final += "and "+ self.weapon_inventory[-1].weapon_name + " Weapon objects"
        return string_final

    def get_winner_of_duel_name(self, opponent):

        
        if self.weapon_inventory == []:

            return opponent.duelist_name
        elif self.weapon_inventory == [] and opponent.weapon_inventory == []:

            return "No contest"

        elif opponent.weapon_inventory == []:
            return self.duelist_name
        
            

        random_weapon = random.choice(self.weapon_inventory)

        random_weapon_1 = random.choice(opponent.weapon_inventory)

        print("Duelist {} picked a {}!".format(self.duelist_name,random_weapon.weapon_name))

        print("Duelist {} picked a {}!".format(opponent.duelist_name,random_weapon_1.weapon_name))   



        if random_weapon_1.strength == random_weapon.strength:
            strength_random = random.random()
            print("Both duelists picked weapons of the same strength! The winner will be decided purely by pseudo-randomly gene")

            if strength_random<0.5:
                return opponent.duelist_name
            return self.duelist_name

        if random_weapon.does_break() == True:
            if random_weapon_1.strength < random_weapon.strength :
                return opponent.duelist_name
                print("{}'s {} broke!".format(self.duelist_name,random_weapon.weapon_name))
            return self.duelist_name
            print("{}'s {} broke!".format(opponent.duelist_name,random_weapon_1.weapon_name))

        if random_weapon_1.does_break() == True:
            if random_weapon.strength < random_weapon_1.strength :            
                return self.duelist_name
                print("{}'s {} broke!".format(opponent.duelist_name,weapon_1.weapon_name))
            return opponent.duelist_name
            print("{}'s {} broke!".format(self.duelist_name,weapon.weapon_name))

def main():
    # Creating my Weapon objects
    weapon_1 = Weapon("Rickenbacker 4001c64", 0.8)
    weapon_2 = Weapon("Hofner 500/1", 0.6)
    weapon_3 = Weapon("Squier VI", 0.4)
    weapon_4 = Weapon("Rickenbacker 330", 0.8)
    weapon_5 = Weapon("Fender Vintera 60s Mustang", 0.6)
    weapon_6 = Weapon("Gretsch 6122", 0.4)
    # Creating my Duelist objects
    bass_player = Duelist("Aki Mizuguchi", [weapon_1, weapon_2, weapon_3])
    guitarist = Duelist("Yori Asanagi", [weapon_4, weapon_5, weapon_6])
    # Testing the get_winner_of_duel_name method of the Duelist object 'bass_player' a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner = bass_player.get_winner_of_duel_name(guitarist)
        print("THE WINNER OF DUEL #{} IS {}!".format(duel_number + 1, winner), end="\n\n")
main()

