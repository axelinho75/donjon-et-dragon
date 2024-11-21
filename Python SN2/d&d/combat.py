from utils import lancer_de
import random
import time 
from colorama import Fore, Style, init
from hero import Hero
from monstre import Monstre

init(autoreset=True)
class Combat: 
    def __init__(self, heros, monstres):
        self.heros = heros
        self.monstres = monstres
        self.ordre_initiative = []

    def lancer_initiative(self):
        for creature in self.heros + self.monstres: 
            creature.initiative = lancer_de(20)
        self.ordre_initiative = sorted(self.heros + self.monstres, key=lambda x: x.initiative, reverse=True)

    def afficher_tour(self):
        print(Fore.YELLOW + "\n=== Ordre d'initiative ===")
        for creature in self.ordre_initiative:
            print(f"{creature.name} : {creature.initiative}")
            time.sleep(1)



    def jouer(self):
        while any(hero.pv > 0 for hero in self.heros) and any(monstre.pv >0 for monstre in self.monstres):
            for creature in self.ordre_initiative:
                print (Fore.CYAN + f"\n === Tour de {creature.name} ===")
                if creature.est_ko():
                    continue

                
                time.sleep(1)
                if isinstance(creature, Hero):
                    print(Fore.GREEN + f"{creature.name} (Héros) prend son tour.")
                    action = input ("Choisissez une action : [A]ttaque, [S]oigner :")
                    if action == "A":
                        cible = self.choisir_cible(self.monstres)
                        creature.attaque(cible, lancer_de)
                    elif action == "S":
                        creature.pv += lancer_de(6)
                        print(f"{creature.name} se soigne et recupere des PV !")
                elif isinstance(creature, Monstre):
                    print(Fore.RED + f"{creature.name} (Monstre) prend son tour.")
                    cible = random.choice([hero for hero in self.heros if not hero.est_ko()])
                    creature.attaque(cible, lancer_de)

                print(Style.RESET_ALL + "-" * 30)
                self.afficher_status_combat()

        if all(monstre.pv <= 0 for monstre in self.monstres):
            print ("\nTous les monstres ont ete vaincus ! Victoire des heros ! ")
        else: 
            print ("\nTous les heros ont ete vaincus ! Defaite ...  ! ")
        time.sleep(2)

    def choisir_cible(self, cibles):
        print("\nChoisissez une cible :")
        for i, cible in enumerate(cibles):
            print(f"{i+1}: {cible.name} - PV = {cible.pv}")
        choix = int (input("Entrez le numero de la cible : ")) -1
        return cibles[choix]
    
    def afficher_status_combat(self):
        print("\n=== Status du combat ===")
        for creature in self.heros + self.monstres:
            creature.afficher_status()
            time.sleep(1)