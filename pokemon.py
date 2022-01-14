import time
import numpy as np
import sys


def delay_print(s):
 
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):

        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health

        self.bars = 20 


    def fight(self, Pokemon2):

        print("-----POKEMONE BATTLE-----")
        print("Pokemon 1:", self.name)
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print("Pokemon 2:", Pokemon2.name)
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        
        version = ['Feu', 'Eau', 'Plante']
        for i,k in enumerate(version):
            if self.types == k:
                
                if Pokemon2.types == k:
                    string_1_attack = '\nCe nest pas très efficace...'
                    string_2_attack = '\nCe nest pas très efficace...'

            
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nCe nest pas très efficace...'
                    string_2_attack = '\ncest super efficace!'

               
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nCest très effiace...!'
                    string_2_attack = '\nCe nest pas très efficace....'


        
       
        while (self.bars > 0) and (Pokemon2.bars > 0):
       
            print(self.name ,"Point de vie :", self.health)
            print(Pokemon2.name ,"Point de vie:", Pokemon2.health)

            print("Go", {self.name}, "!")
            for i, x in enumerate(self.moves):
                print(i+1, x)
            index = int(input('choisir une attaque: '))
            print(self.name ,"Utilise", self.moves[index-1])
            time.sleep(1)
            delay_print(string_1_attack)

        
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(self.name ,"Point de vie:", self.health)
            print(Pokemon2.name ,"point de vie:", Pokemon2.health)
            time.sleep(.5)

         
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' est mort.')
                break

           
            print("Go",  Pokemon2.name, "!")
            for i, x in enumerate(Pokemon2.moves):
                print(i+1, x)
            index = int(input('Choisi une ataque: '))
            print(Pokemon2.name ,"utilise", Pokemon2.moves[index-1])
            time.sleep(1)
            delay_print(string_2_attack)

          
            self.bars -= Pokemon2.attack
            self.health = ""

           
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(self.name ,"Point de vie:", self.health)
            print(Pokemon2.name ,"Point de vie:", Pokemon2.health)
            time.sleep(.5)

          
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' est mort.')
                break






if __name__ == '__main__':

    Dracaufeu = Pokemon('Dracaufeu', 'Feu', ['Lance flamme', 'Vol', 'Flameche', 'Poing de feu'], {'ATTACK':12, 'DEFENSE': 8})
    Tortank = Pokemon('Tortank', 'Eau', ['Pistolet à eau', 'Bulle deau', 'Canon a eau', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Florizarre = Pokemon('Florizarre', 'Plante', ['Fouet lianne', 'feuille herbe', 'Seisme', 'Lance soleil'],{'ATTACK':8, 'DEFENSE':12})

    Salameche = Pokemon('Salameche', 'Feu', ['flamche', 'Griffe', 'coup de queu', 'Poing de feu'],{'ATTACK':4, 'DEFENSE':2})
    carapuce = Pokemon('carapuce', 'Eau', ['Bulle deau', 'Belier', 'coup de tete', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    bulbizarre = Pokemon('bulbizarre', 'Plante', ['Charge', 'Tranche herbe', 'fouet lianne', 'Vampigraine'],{'ATTACK':2, 'DEFENSE':4})

    Reptincelle = Pokemon('Reptincelle', 'Feu', ['flameche', 'Griffe', 'lance flamme', 'Poing de feu'],{'ATTACK':6, 'DEFENSE':5})
    Carabaffe = Pokemon('Carabaffe', 'Eau', ['bulle deau', 'pistolet a eau', 'Coup de tete', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Herbizarre = Pokemon('Herbizarre', 'Plante', ['Tranche herbe', 'Fouet lianne', 'vampigraine', 'charge'],{'ATTACK':4, 'DEFENSE':6})


    Reptincelle.fight(Carabaffe)