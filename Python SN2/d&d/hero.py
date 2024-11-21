from Creature import creature

class Hero(creature):
    def __init__(self, nom, description, pv, defense, degatsmax, typedegats, arme, etat, initiative): 
        super().__init__(nom, description, pv, defense, degatsmax, typedegats, etat, initiative)
        self.arme = arme
        self.inventaire = []


    def afficher_status(self):
        super().afficher_status()
        print(f"Arme : {self.arme} - Inventaire : {self.inventaire if self.inventaire else 'Vide'}")

    