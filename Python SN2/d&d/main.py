from hero import Hero
from monstre import Monstre 
from combat import Combat


def initialiser_jeu():
    hero =[
        Hero("Guerrier", "Un vaillant combattant", 30, 15, 8, "Tranchant", "Epee", [], 10),
        Hero("Mage", "Un maîtres des arcanes", 20, 12, 5, "Feu", "Batôn magique", [], 10 )
    ]

    monstre =[
        Monstre("Gobelin", "Un petit ennemie sournois", 15, 10, 6, "Percant", ["Feu"], 5),
        Monstre("Troll", "Un geant effrayant", 40, 14, 10, "Contondant", ["Tranchant"], 2)
    ]

    combat = Combat(hero, monstre)
    combat.lancer_initiative()
    combat.afficher_tour()
    combat.jouer()

if __name__ == "__main__":
    initialiser_jeu()

